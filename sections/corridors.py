import streamlit as st
import plotly.graph_objects as go
import pandas as pd


CORREDORES = [
    {
        "origen": "MICHOACAN", "ciudad_origen": "Uruapan",
        "producto": "Aguacate 81% · 2.77M ton/año",
        "cruce": "LAREDO, TX", "flujo_cruce": "$4.2B/año · 7.35M movimientos · 6 VIPs, 3 cold storage",
        "destino": "Texas, Centro, Este USA", "transito": "2 dias transito",
        "valor": 4200,
    },
    {
        "origen": "SINALOA", "ciudad_origen": "Culiacan",
        "producto": "Tomate/Pimientos · 25,584 ha",
        "cruce": "NOGALES, AZ", "flujo_cruce": "$2.5B/año · 120K camiones/año · 4 VIPs, 2 cold storage",
        "destino": "Arizona, California, Midwest", "transito": "12-18 hrs transito",
        "valor": 2500,
    },
    {
        "origen": "JALISCO", "ciudad_origen": "Guadalajara",
        "producto": "Flores/Berries · exportacion diversificada",
        "cruce": "PHARR-REYNOSA", "flujo_cruce": "$1.8B/año · 55K camiones/año · 3 VIPs, 2 cold storage",
        "destino": "Texas, Este USA", "transito": "1-2 dias transito",
        "valor": 1800,
    },
    {
        "origen": "BAJA CALIFORNIA", "ciudad_origen": "Ensenada",
        "producto": "Hortalizas/Uva · exportacion costera",
        "cruce": "OTAY MESA", "flujo_cruce": "$1.1B/año · 40K camiones/año · 2 VIPs, 1 cold storage",
        "destino": "California", "transito": "Same day transito",
        "valor": 1100,
    },
]


def tarjeta_corredor(c):
    with st.container(border=True):
        col1, col_arrow1, col2, col_arrow2, col3 = st.columns([3, 0.5, 4, 0.5, 3])

        with col1:
            st.markdown("**MX ORIGEN**")
            st.markdown(f"### {c['origen']}")
            st.markdown(f"**{c['ciudad_origen']}**")
            st.caption(c["producto"])

        with col_arrow1:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.markdown("## →")

        with col2:
            st.markdown("**CRUCE FRONTERIZO**")
            st.markdown(f"### {c['cruce']}")
            st.caption(c["flujo_cruce"])

        with col_arrow2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.markdown("## →")

        with col3:
            st.markdown("**USA DESTINO**")
            st.markdown(f"**{c['destino']}**")
            st.markdown(f"{c['transito']}")


def show_corridors():
    st.header("Corredores Logisticos Criticos")
    st.markdown("**75% del volumen total cruza por estos 4 corredores principales**")

    # --- Tarjetas de flujo ---
    st.subheader("Flujos Principales Mexico → USA")
    for c in CORREDORES:
        tarjeta_corredor(c)

    st.markdown("---")

    # --- Grafica de barras horizontales ---
    st.subheader("Flujo por Corredor (millones USD/año)")
    fig = go.Figure(go.Bar(
        x=[c["valor"] for c in CORREDORES],
        y=[c["cruce"] for c in CORREDORES],
        orientation="h",
        marker_color=["#022A6F", "#2796B7", "#629D3E", "#64748b"],
        text=[f"${c['valor']/1000:.1f}B" for c in CORREDORES],
        textposition="outside",
    ))
    fig.update_layout(
        xaxis_title="Millones USD/año",
        height=320,
        template="plotly_white",
        margin=dict(l=20, r=60, t=20, b=20),
        xaxis=dict(range=[0, 5500]),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("**Oportunidad CL Circular:** Laredo TX concentra 42% del valor total. Prioridad #1 para operaciones de agencia aduanal.")

    # --- Tabla corredores ---
    st.subheader("Ranking de Corredores por Volumen")
    corredores = pd.DataFrame([
        ["Michoacan → Laredo, TX", "Aguacate", "$4.2B/año", "6 VIPs · 3 cold storage", "2 dias", "CRITICO"],
        ["Jalisco → Pharr-Reynosa", "Berries/Aguacate", "$4.5B/año", "Cold storage moderno", "<2 dias", "CRECIENTE"],
        ["Sinaloa → Nogales, AZ", "Tomate/Pimientos", "$2.5B/año", "4 VIPs · 2 cold storage", "12-18 hrs", "CRITICO"],
        ["Baja California → Otay Mesa", "Varios", "Significativo", "Infraestructura costa", "<2 hrs", "ESTRATEGICO"],
        ["Varios → Colombia Bridge", "Aguacate/Frutas", "Parte Laredo", "FAST Lane pre-clearance", "Similar Laredo", "EFICIENCIA"],
    ], columns=["Corredor", "Commodity Principal", "Volumen/Año", "Infraestructura", "Transito", "Prioridad CL Circular"])
    st.dataframe(corredores, use_container_width=True, hide_index=True)

    # --- Pain points ---
    st.subheader("Pain Points = Oportunidades CL Circular")
    risks = [
        ("1. Perdida trazabilidad en transito", "12-48hrs sin visibilidad real-time temperatura en cruce", "Sensores GPS+temp con alertas y reportes auto-FSMA"),
        ("2. Congestion en cruces fronterizos", "Esperas 2-8hrs peak season → perdida cadena fria", "Alerts congestion → rerouting automatico"),
        ("3. Compliance FSMA", "Temperature monitoring obligatorio, metodos manuales = rechazos +40%", "Compliance automatico con API FDA"),
        ("4. Robo de carga", "Michoacan/Sinaloa: aguacate = target crimen organizado", "GPS activo, geofence alerts, recuperacion asistida"),
        ("5. Clima impredecible", "Lluvias Sinaloa dic-mar, heladas Michoacan ene-feb", "Predictive alerts + recomendaciones rerouting"),
    ]
    for titulo, problema, solucion in risks:
        with st.expander(titulo):
            st.warning(f"**Problema:** {problema}")
            st.success(f"**Solucion CL Circular:** {solucion}")
