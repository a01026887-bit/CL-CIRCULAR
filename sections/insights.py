import streamlit as st
import plotly.graph_objects as go

def show_insights():
    st.header(" Strategic Insights")

    tab1, tab2, tab3 = st.tabs([" Oportunidades", " Riesgos", " Plan de Entrada"])

    with tab1:
        oportunidades = [
            ("1️⃣ Partnership APEAM", "29K productores, 90 empaques cert., 100K+ embarques/año", "Piloto gratuito 3–5 empaques · Presentación asamblea APEAM", "$500K–1M Año 1"),
            ("2️⃣ White-Label Transportistas", "Transportistas pierden clientes por daño temp, FSMA = liability", "Target operadores Laredo/Nogales >50 camiones, revenue-share 60/40", "$3–9M/año · 5 operadores"),
            ("3️⃣ Integración ERP Sysco/US Foods", "Foodservice necesita visibilidad supply chain + ESG reporting", "API CL→SAP/Oracle · Piloto Sysco FreshPoint Q1 2026", "Enterprise $200–500/embarque"),
            ("4️⃣ Nicho Premium Flores", "Flores mueren en 24–36hrs · Margen alto = disposición pagar", "Pricing $150–250/embarque · Target Edo. México/Morelos", "$300–500K/año nicho rentable"),
            ("5️⃣ Berries Congelados", "Cold chain más estricto (−18 a −23°C) · Menor competencia", "Sensor variant -30°C · Target Jalisco frozen · Ruta→Otay Mesa", "$125–750K/año"),
        ]
        for titulo, razon, tactica, potencial in oportunidades:
            with st.expander(titulo):
                st.info(f"**Razón:** {razon}")
                st.success(f"**Táctica:** {tactica}")
                st.metric("Potencial", potencial)

    with tab2:
        riesgos = [
            ("1️⃣ Competencia Establecida", "🔴 ALTO", "🟡 MEDIA", "Sensitech/Tive ya trabajan con grandes, más capital", "Pricing 50% menor · Soporte español 24/7 · Focus nicho medianos"),
            ("2️⃣ Adopción Lenta Pequeños Productores", "🟡 MEDIO", "🔴 ALTA", "Mayoría <50 ha, resistencia cambio, percepción costo alto", "Freemium 10 embarques · Partnership cooperativas"),
            ("3️⃣ Robo/Pérdida Sensores", "🟡 MEDIO", "🟡 MEDIA", "Cargo theft Michoacán/Sinaloa, sensores robados con carga", "Depósito $50/sensor · GPS activo · Design discreto"),
            ("4️⃣ Falta Conectividad Rural", "🔴 ALTO", "🟡 MEDIA", "Michoacán montañas, Sinaloa costa: GSM irregular", "Data logging offline 7 días · Satellite fallback Iridium"),
            ("5️⃣ Cambio Regulatorio Arancelario", "🔴 ALTO", "🟢 BAJA", "USMCA renewal 2026, posibles aranceles = colapso TAM", "Diversificación MX→Canadá · Pivot plan MX domestic"),
        ]
        for titulo, impacto, prob, problema, mitigacion in riesgos:
            with st.expander(titulo):
                col1, col2 = st.columns(2)
                col1.metric("Impacto", impacto)
                col2.metric("Probabilidad", prob)
                st.warning(f"**Problema:** {problema}")
                st.success(f"**Mitigación:** {mitigacion}")

    with tab3:
        fases = [
            ("🏗️ FASE 1 — Fundación (Meses 1–6)", "#3b82f6",
             ["Oficina Uruapan, 3 staff, $200K setup",
              "Pilotos APEAM: 3–5 empaques, 100 sensores gratis",
              "Validación técnica: −10°C a +40°C, batería 14 días",
              "Dashboard MVP: alertas real-time, español/inglés"],
             "500–1,000 sensores · 3–5 pilotos · 3 meses data"),
            ("🚀 FASE 2 — Escala Aguacate (Meses 7–12)", "#0891b2",
             ["Peak Q1: 1,500–2,000 sensores inventory",
              "2–3 transportistas Laredo, revenue-share 60/40",
              "Case studies, PMA Foodservice, trade press",
              "Fundraising Serie A: $3–5M USD"],
             "15–20 clientes · 10–15K embarques · $750K–1.5M revenue"),
            ("🌱 FASE 3 — Expansión Vertical (Meses 13–24)", "#059669",
             ["Berries Jalisco: Driscoll's growers, FD Berries",
              "Mango Nayarit: EMEX, NayAgra, temporada abr–sep",
              "Pilotos tomate: CAADES greenhouse, Sinaloa→Nogales",
              "ERP Integration: API Sysco/US Foods, enterprise pricing"],
             "50–70 clientes · 40–60K embarques · $2.5–4M revenue"),
        ] 
        for titulo, color, acciones, kpi in fases:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}dd, {color});
                        padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 1rem;">
                <h3 style="color:white; margin-bottom:1rem;">{titulo}</h3>
                <ul>{"".join(f"<li>{a}</li>" for a in acciones)}</ul>
                <p style="margin-top:1rem; padding-top:1rem; border-top:1px solid rgba(255,255,255,0.3);">
                    <b>KPIs:</b> {kpi}
                </p>
            </div>""", unsafe_allow_html=True)

        # Proyección financiera
        st.subheader("📊 Proyección Financiera 3 Años")
        fig = go.Figure()
        anios = ["Año 1 (2026)", "Año 2 (2027)", "Año 3 (2028)"]
        rev_min = [0.75, 3.6, 8.0]
        rev_max = [1.1, 5.4, 12.0]
        fig.add_trace(go.Bar(name="Revenue Mínimo", x=anios, y=rev_min, marker_color="#38bdf8"))
        fig.add_trace(go.Bar(name="Revenue Máximo", x=anios, y=rev_max, marker_color="#0284c7"))
        fig.update_layout(barmode="group", yaxis_title="USD Millions", height=380)
        st.plotly_chart(fig, use_container_width=True)
