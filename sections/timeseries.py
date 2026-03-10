import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

def show_timeseries():
    st.header("Pronóstico de Series de Tiempo")
    st.markdown("Modelos ARIMA ajustados por categoría · México → USA · 2015–2026")

    # --- Cargar datos ---
    excel_path = "Base de datos Buena CL Circular.xlsx"

    try:
        xls = pd.ExcelFile(excel_path)
    except FileNotFoundError:
        st.error("No se encontró el archivo 'Base de datos Buena CL Circular.xlsx'. Asegúrate de subirlo al repo.")
        return

    categorias = {
        "Frutas":   {"sheet": "Frutas",  "order": (11, 1, 8),  "color": "#4ADE80"},
        "Verduras": {"sheet": "Verdura", "order": (7,  1, 7),  "color": "#38BDF8"},
        "Flores":   {"sheet": "Flores",  "order": (10, 1, 11), "color": "#F472B6"},
    }

    # --- Selector de categoría ---
    categoria = st.selectbox("Selecciona categoría", list(categorias.keys()))
    cfg = categorias[categoria]

    # --- Cargar y preparar datos ---
    df = pd.read_excel(xls, sheet_name=cfg["sheet"])
    df["date"] = pd.to_datetime(
        df["refYear"].astype(str) + "-" + df["refMonth"].astype(str).str.zfill(2) + "-01"
    )
    df = df.sort_values("date").set_index("date")
    serie = df["primaryValue"]

    # --- Ajustar modelo ARIMA ---
    with st.spinner(f"Ajustando modelo ARIMA{cfg['order']} para {categoria}..."):
        modelo = ARIMA(serie, order=cfg["order"])
        resultado = modelo.fit()
        forecast = resultado.get_forecast(steps=12)
        pred_mean = forecast.predicted_mean
        pred_ci   = forecast.conf_int()

    # --- Gráfico ---
    fig = go.Figure()

    # Datos históricos
    fig.add_trace(go.Scatter(
        x=serie.index, y=serie.values,
        name="Histórico",
        line=dict(color="#0B7285", width=2),
    ))

    # Pronóstico
    fig.add_trace(go.Scatter(
        x=pred_mean.index, y=pred_mean.values,
        name="Pronóstico 2026",
        line=dict(color=cfg["color"], width=2, dash="dash"),
    ))

    # Banda de confianza
    fig.add_trace(go.Scatter(
        x=list(pred_ci.index) + list(pred_ci.index[::-1]),
        y=list(pred_ci.iloc[:, 1]) + list(pred_ci.iloc[:, 0][::-1]),
        fill="toself",
        fillcolor=cfg["color"].replace(")", ", 0.15)").replace("rgb", "rgba"),
        line=dict(color="rgba(0,0,0,0)"),
        name="Intervalo de confianza 95%",
    ))

    fig.update_layout(
        title=f"{categoria} — ARIMA{cfg['order']}",
        xaxis_title="Fecha",
        yaxis_title="Valor (USD)",
        template="plotly_white",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- Métricas ---
    col1, col2, col3 = st.columns(3)
    fitted = resultado.fittedvalues
    mae  = np.mean(np.abs(serie - fitted))
    mape = np.mean(np.abs((serie - fitted) / serie)) * 100
    col1.metric("MAE", f"{mae:,.0f}")
    col2.metric("MAPE", f"{mape:.2f}%")
    col3.metric("Modelo", f"ARIMA{cfg['order']}")

    # --- Tabla de pronóstico ---
    st.subheader("Pronóstico mensual 2026")
    df_forecast = pd.DataFrame({
        "Mes": pred_mean.index.strftime("%B %Y"),
        "Valor Estimado (USD)": pred_mean.values.astype(int),
        "Límite Inferior": pred_ci.iloc[:, 0].values.astype(int),
        "Límite Superior": pred_ci.iloc[:, 1].values.astype(int),
    })
    st.dataframe(df_forecast, use_container_width=True)
