import streamlit as st
import plotly.graph_objects as go

def show_executive():
    st.header("Executive Summary")

    # --- KPIs ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Volumen Total Mercado", "$28–30B USD", "2025")
    col2.metric("Embarques Estimados", "~450K", "cargas/año")
    col3.metric("Concentración Geográfica", "75%", "3 cruces frontera")

    col5, col6 = st.columns(2)
    col5.metric("Mejor Predictibilidad", "8.89% MAPE", "HS08 Frutas")
    col6.metric("Crecimiento 2015–2025", "+34%", "HS08")

    st.markdown("---")

    # --- Recomendación Estratégica ---
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0284c7, #38bdf8);
                padding: 2rem; border-radius: 12px; color: white; margin-bottom: 1.5rem;">
        <h2 style="color:white;">🎯 Recomendación Estratégica para CL Circular</h2>
        <h3 style="color:#f0f9ff;">PRIORIDAD #1: HS08 (FRUTAS) — AGUACATE COMO BEACHHEAD</h3>
        <ul>
            <li><b>Predictibilidad:</b> MAPE 8.89% (menor riesgo operacional vs HS07: 21.52%)</li>
            <li><b>Volumen concentrado:</b> 100,000+ embarques aguacate/año</li>
            <li><b>Geografía focalizada:</b> Michoacán/Jalisco → Laredo/Nogales</li>
            <li><b>ROI demostrable:</b> Pérdida por temperatura = $5–15K/camión vs sensor $50–150</li>
            <li><b>Compliance pressure:</b> USDA/FSMA enforcement creciente</li>
            <li><b>Timing:</b> Pico Q1 (ene–abr) = 85% embarques anuales</li>
        </ul>
        <p><b>Meta Año 1:</b> 1,500–2,000 sensores · 5–10% penetración aguacate · Revenue $750K–$1.5M USD</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Ranking commodities ---
    st.subheader(" Top Commodities por Volumen y TAM")

    commodities = {
        "Commodity": [" Aguacate (HS08)", " Tomate (HS07)", " Pimientos (HS07)", " Mango (HS08)", " Berries (HS08)"],
        "Volumen/Año": ["2.77M ton", "3M ton", "1.5M ton", "415K ton", "566K ton"],
        "Embarques": ["100K+", "150K+", "75K+", "21K+", "15K+"],
        "TAM Estimado": ["$5–15M", "$7.5–22.5M", "$3.75–11.25M", "$1.05–3.15M", "$0.75–2.25M"],
        "Cold Chain": [" CRÍTICO", " CRÍTICO", " CRÍTICO", " ALTO", " CRÍTICO"]
    }

    import pandas as pd
    df = pd.DataFrame(commodities)
    st.dataframe(df, use_container_width=True, hide_index=True)
