import streamlit as st
import plotly.graph_objects as go


CORREDORES = [
    {
        "origen": "MICHOACÁN", "ciudad_origen": "Uruapan",
        "producto": "Aguacate 81% · 2.77M ton/año",
        "cruce": "LAREDO, TX", "flujo_cruce": "$4.2B/año · 7.35M movimientos · 6 VIPs, 3 cold storage",
        "destino": "Texas, Centro, Este USA", "transito": "2 días tránsito",
        "valor": 4200,
    },
    {
        "origen": "SINALOA", "ciudad_origen": "Culiacán",
        "producto": "Tomate/Pimientos · 25,584 ha",
        "cruce": "NOGALES, AZ", "flujo_cruce": "$2.5B/año · 120K camiones/año · 4 VIPs, 2 cold storage",
        "destino": "Arizona, California, Midwest", "transito": "12-18 hrs tránsito",
        "valor": 2500,
    },
    {
        "origen": "JALISCO", "ciudad_origen": "Guadalajara",
        "producto": "Flores/Berries · exportación diversificada",
        "cruce": "PHARR-REYNOSA", "flujo_cruce": "$1.8B/año · 55K camiones/año · 3 VIPs, 2 cold storage",
        "destino": "Texas, Este USA", "transito": "1-2 días tránsito",
        "valor": 1800,
    },
    {
        "origen": "BAJA CALIFORNIA", "ciudad_origen": "Ensenada",
        "producto": "Hortalizas/Uva · exportación costera",
        "cruce": "OTAY MESA", "flujo_cruce": "$1.1B/año · 40K camiones/año · 2 VIPs, 1 cold storage",
        "destino": "California", "transito": "Same day tránsito",
        "valor": 1100,
    },
]


def tarjeta_corredor(c):
    st.markdown(
        f"""
        <div style="
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 1rem;
        ">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">

                <!-- ORIGEN -->
                <div style="text-align: center; min-width: 160px;">
                    <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">🇲🇽 ORIGEN</div>
                    <div style="font-size: 1rem; font-weight: 700; color: #022A6F;">{c['origen']}</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #1e293b; margin-top: 4px;">{c['ciudad_origen']}</div>
                    <div style="font-size: 0.80rem; color: #475569; margin-top: 4px;">{c['producto']}</div>
                </div>

                <!-- FLECHA -->
                <div style="font-size: 1.5rem; color: #2796B7;">→</div>

                <!-- CRUCE -->
                <div style="text-align: center; min-width: 200px;">
                    <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">🚛 CRUCE FRONTERIZO</div>
                    <div style="font-size: 1rem; font-weight: 700; color: #2796B7;">{c['cruce']}</div>
                    <div style="font-size: 0.80rem; color: #475569; margin-top: 4px;">{c['flujo_cruce']}</div>
                </div>

                <!-- FLECHA -->
                <div style="font-size: 1.5rem; color: #2796B7;">→</div>

                <!-- DESTINO -->
                <div style="text-align: center; min-width: 160px;">
                    <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">🇺🇸 DESTINO</div>
                    <div style="font-size: 1rem; font-weight: 700; color: #629D3E;">DESTINO</div>
                    <div style="font-size: 0.85rem; color: #1e293b; margin-top: 4px;">{c['destino']}</div>
                    <div style="font-size: 0.80rem; font-weight: 600; color: #022A6F; margin-top: 4px;">{c['transito']}</div>
                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_corridors():
    st.header("Corredores Logisticos Criticos")
    st.markdown("**75% del volumen total cruza por estos 4 corredores principales**")

    # --- Tarjetas de flujo ---
    st.subheader("Flujos Principales Mexico → USA")
    for c in CORREDORES:
        tarjeta_corredor(c)

    st.markdown("---")

    # --- Gráfica de barras horizontales ---
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
    import pandas as pd
    corredores = pd.DataFrame([
        ["Michoacán → Laredo, TX","Aguacate","$4.2B/año","6 VIPs · 3 cold storage","2 días","🔴 CRÍTICO"],
        ["Jalisco → Pharr-Reynosa","Berries/Aguacate","$4.5B/año","Cold storage moderno","<2 días","🟠 CRECIENTE"],
        ["Sinaloa → Nogales, AZ","Tomate/Pimientos","$2.5B/año","4 VIPs · 2 cold storage","12–18 hrs","🔴 CRÍTICO"],
        ["Baja California → Otay Mesa","Varios","Significativo","Infraestructura costa","<2 hrs","🟡 ESTRATÉGICO"],
        ["Varios → Colombia Bridge","Aguacate/Frutas","Parte Laredo","FAST Lane pre-clearance","Similar Laredo","🟡 EFICIENCIA"],
    ], columns=["Corredor","Commodity Principal","Volumen/Año","Infraestructura","Tránsito","Prioridad CL Circular"])
    st.dataframe(corredores, use_container_width=True, hide_index=True)

    # --- Pain points ---
    st.subheader("Pain Points = Oportunidades CL Circular")
    risks = [
        ("1️⃣ Pérdida trazabilidad en tránsito", "12–48hrs sin visibilidad real-time temperatura en cruce", "Sensores GPS+temp con alertas y reportes auto-FSMA"),
        ("2️⃣ Congestión en cruces fronterizos", "Esperas 2–8hrs peak season → pérdida cadena fría", "Alerts congestión → rerouting automático"),
        ("3️⃣ Compliance FSMA", "Temperature monitoring obligatorio, métodos manuales = rechazos +40%", "Compliance automático con API FDA"),
        ("4️⃣ Robo de carga", "Michoacán/Sinaloa: aguacate = target crimen organizado", "GPS activo, geofence alerts, recuperación asistida"),
        ("5️⃣ Clima impredecible", "Lluvias Sinaloa dic–mar, heladas Michoacán ene–feb", "Predictive alerts + recomendaciones rerouting"),
    ]
    for titulo, problema, solucion in risks:
        with st.expander(titulo):
            st.warning(f"**Problema:** {problema}")
            st.success(f"** Solución CL Circular:** {solucion}")
