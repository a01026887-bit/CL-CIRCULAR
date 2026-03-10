import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

CATEGORIAS = {
    "Frutas":   {"sheet": "Frutas",  "order": (11, 1, 8),  "color": "#4ADE80", "mape": 8.89,  "mae": 55744310,  "rmse": 66517110},
   "Verduras": {"sheet": "Verduras", "order": (7,  1, 7),  "color": "#38BDF8", "mape": 21.52, "mae": 140022500, "rmse": 149741500},
    "Flores":   {"sheet": "Flores",  "order": (10, 1, 11), "color": "#F472B6", "mape": 11.68, "mae": 880264,    "rmse": 924303},
    "Total":    {"sheet": None,      "order": (12, 1, 1),  "color": "#FBBF24", "mape": 16.86, "mae": 224940500, "rmse": 247287700},
}

def cargar_serie(xls, cfg, dfs):
    if cfg["sheet"] is None:
        total = sum(dfs[k] for k in ["Frutas", "Verduras", "Flores"])
        return total
    df = pd.read_excel(xls, sheet_name=cfg["sheet"])
    df["date"] = pd.to_datetime(
        df["refYear"].astype(str) + "-" + df["refMonth"].astype(str).str.zfill(2) + "-01"
    )
    df = df.sort_values("date").set_index("date")
    return df["primaryValue"]

def grafico_categoria(nombre, serie, cfg):
    modelo = ARIMA(serie, order=cfg["order"])
    resultado = modelo.fit()
    forecast = resultado.get_forecast(steps=12)
    pred_mean = forecast.predicted_mean
    pred_ci = forecast.conf_int()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=serie.index, y=serie.values,
        name="Historico",
        line=dict(color="#0B7285", width=2),
    ))
    fig.add_trace(go.Scatter(
        x=pred_mean.index, y=pred_mean.values,
        name="Pronostico 2026",
        line=dict(color=cfg["color"], width=2.5, dash="dash"),
    ))
    fig.add_trace(go.Scatter(
        x=list(pred_ci.index) + list(pred_ci.index[::-1]),
        y=list(pred_ci.iloc[:, 1]) + list(pred_ci.iloc[:, 0][::-1]),
        fill="toself",
        fillcolor="rgba(100,200,255,0.10)",
        line=dict(color="rgba(0,0,0,0)"),
        name="Intervalo 95%",
    ))
    fig.update_layout(
        title=f"{nombre} — ARIMA{cfg['order']}",
        xaxis_title="Fecha",
        yaxis_title="USD",
        template="plotly_white",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        height=420,
    )
    return fig, pred_mean, pred_ci, resultado

def show_timeseries():
    st.header("Pronostico de Series de Tiempo")
    st.markdown("Modelos ARIMA ajustados por categoria · Mexico → USA · HS06/07/08 · 2015–2026")

    excel_path = "Base de datos Buena CL Circular.xlsx"
    try:
        xls = pd.ExcelFile(excel_path)
    except FileNotFoundError:
        st.error("No se encontro el archivo 'Base de datos Buena CL Circular.xlsx'. Subelo a la raiz del repo.")
        return

    # Cargar las 3 series base
    series = {}
    for nombre in ["Frutas", "Verduras", "Flores"]:
        cfg = CATEGORIAS[nombre]
        df = pd.read_excel(xls, sheet_name=cfg["sheet"])
        df["date"] = pd.to_datetime(
            df["refYear"].astype(str) + "-" + df["refMonth"].astype(str).str.zfill(2) + "-01"
        )
        df = df.sort_values("date").set_index("date")
        series[nombre] = df["primaryValue"]

    # Serie Total = suma de las 3
    series["Total"] = series["Frutas"] + series["Verduras"] + series["Flores"]

    # --- Tabla resumen de metricas ---
    st.subheader("Resumen de Modelos ARIMA")
    metricas = []
    for nombre, cfg in CATEGORIAS.items():
        metricas.append({
            "Categoria": nombre,
            "Modelo": f"ARIMA{cfg['order']}",
            "MAE": f"{cfg['mae']:,.0f}",
            "RMSE": f"{cfg['rmse']:,.0f}",
            "MAPE (%)": f"{cfg['mape']:.2f}%",
        })
    st.dataframe(pd.DataFrame(metricas), use_container_width=True, hide_index=True)

    st.markdown("---")

    # --- Graficos y pronosticos por categoria ---
    tabs = st.tabs(["Frutas", "Verduras", "Flores", "Total"])

    for i, (nombre, tab) in enumerate(zip(CATEGORIAS.keys(), tabs)):
        cfg = CATEGORIAS[nombre]
        with tab:
            with st.spinner(f"Ajustando modelo para {nombre}..."):
                fig, pred_mean, pred_ci, resultado = grafico_categoria(nombre, series[nombre], cfg)

            # Metricas rapidas
            col1, col2, col3 = st.columns(3)
            col1.metric("MAPE", f"{cfg['mape']:.2f}%")
            col2.metric("MAE", f"{cfg['mae']:,.0f} USD")
            col3.metric("Modelo", f"ARIMA{cfg['order']}")

            # Grafico
            st.plotly_chart(fig, use_container_width=True)

            # Tabla de pronostico mensual
            st.subheader(f"Pronostico mensual 2026 — {nombre}")
            df_fc = pd.DataFrame({
                "Mes": pred_mean.index.strftime("%B %Y"),
                "Valor Estimado (USD)": pred_mean.values.round(0).astype(int),
                "Limite Inferior (USD)": pred_ci.iloc[:, 0].values.round(0).astype(int),
                "Limite Superior (USD)": pred_ci.iloc[:, 1].values.round(0).astype(int),
            })
            st.dataframe(df_fc, use_container_width=True, hide_index=True)
