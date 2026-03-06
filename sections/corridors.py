import streamlit as st
import plotly.graph_objects as go

def show_corridors():
    st.header("🚚 Corredores Logísticos Críticos")

    # --- Sankey diagram ---
    st.subheader("Flujo México → USA por Corredor Principal")

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15, thickness=20,
            label=["Michoacán","Sinaloa","Jalisco","Baja Calif.",
                   "Laredo TX","Nogales AZ","Pharr-Reynosa","Otay Mesa",
                   "Texas/Centro USA","Arizona/California","Texas/Este USA","California"],
            color=["#16a34a","#16a34a","#16a34a","#16a34a",
                   "#0284c7","#0284c7","#0284c7","#0284c7",
                   "#f97316","#f97316","#f97316","#f97316"]
        ),
        link=dict(
            source=[0,1,2,3, 4,5,6,7],
            target=[4,5,6,7, 8,9,10,11],
            value=[4200,2500,4500,1200, 4200,2500,4500,1200],
            color=["rgba(56,189,248,0.4)"]*8
        )
    )])
    fig.update_layout(title="Flujo por Corredor (millones USD/año)", height=450)
    st.plotly_chart(fig, use_container_width=True)

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
    st.subheader("⚠️ Pain Points = Oportunidades CL Circular")
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
            st.success(f"**🎯 Solución CL Circular:** {solucion}")
