import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show_coldchain():
    st.header("❄️ Cold Chain & Compliance")

    # --- Tabla criticidad ---
    st.subheader("Necesidades de Trazabilidad por Commodity")

    cc = pd.DataFrame([
        ["🫐 Berries",  "0–2°C",   "90–95%", "<12 hrs",  "$8–12K",  "CRÍTICO"],
        ["🌹 Flores",   "2–5°C",   "80–95%", "<24 hrs",  "$5–10K",  "RECOMENDADO"],
        ["🥑 Aguacate", "5–7°C",   "85–90%", "24–48 hrs","$5–15K",  "CRÍTICO"],
        ["🍅 Tomate",   "12–15°C", "90–95%", "24–48 hrs","$8–15K",  "CRÍTICO"],
        ["🥭 Mango",    "10–13°C", "85–90%", "48–72 hrs","$6–12K",  "RECOMENDADO"],
        ["🫑 Pimientos","7–10°C",  "90–95%", "48 hrs",   "$8–12K",  "CRÍTICO"],
    ], columns=["Commodity","Temp Crítica","Humedad Óptima","Máx sin Monitoreo","Pérdida/Embarque","FSMA"])
    st.dataframe(cc, use_container_width=True, hide_index=True)

    st.error("⚠️ 66% de los commodities top requieren FSMA obligatorio. Pérdida $5–15K/embarque vs sensor $50–150 = **ROI 33–100x**")

    # --- Inversión cold chain ---
    st.subheader("Inversión en Cold Chain México (USD Billions)")
    fig = go.Figure(go.Bar(
        x=["2020", "2025", "2030*"],
        y=[1.2, 2.1, 3.8],
        marker_color=["#64748b", "#38bdf8", "#10b981"],
        text=["$1.2B", "$2.1B", "$3.8B*"],
        textposition="outside"
    ))
    fig.update_layout(yaxis_title="USD Billions", height=350)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("CAGR 2020–2030 estimado: ~12% anual. *Proyección.")
