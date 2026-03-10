import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def show_market():
    st.header(" Panorama de Mercado")

    # --- Distribución por capítulo HS ---
    st.subheader("Distribución del Mercado por Capítulo HS (2025)")

    fig_pie = go.Figure(data=[go.Pie(
        labels=["HS08 Frutas", "HS07 Verduras", "Otros Perecederos", "HS06 Flores"],
        values=[42, 36, 21, 1],
        hole=0.4,
        marker_colors=["#38bdf8", "#f97316", "#64748b", "#ec4899"]
    )])
    fig_pie.update_layout(
        title="Participación por Capítulo HS — Mercado $28–30B USD",
        height=400
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # --- Estacionalidad HS08 ---
    st.subheader("Estacionalidad Proyectada 2026 (HS08 – Frutas)")

    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    valores = [1.7, 1.6, 1.55, 1.5, 1.4, 1.35, 1.3, 1.3, 1.45, 1.5, 1.55, 1.6]

    fig_bar = go.Figure(go.Bar(
        x=meses, y=valores,
        marker_color=["#ef4444","#ef4444","#f97316","#f97316",
                      "#f59e0b","#f59e0b","#64748b","#64748b",
                      "#f97316","#f97316","#f97316","#ef4444"],
        text=[f"${v}B" for v in valores],
        textposition="outside"
    ))
    fig_bar.update_layout(
        yaxis_title="Valor estimado (USD Billions)",
        height=400
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    st.info("🎯 **Implicación CL Circular:** Q1 (ene–abr) concentra 85% de embarques anuales de aguacate. Onboarding crítico: sep–dic 2025.")
