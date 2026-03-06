import streamlit as st

# --- Configuración de página ---
st.set_page_config(
    page_title="CL Circular – Dashboard Estratégico",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Importar secciones ---
from sections.executive import show_executive
from sections.market_overview import show_market
from sections.market_players import show_players
from sections.corridors import show_corridors
from sections.coldchain import show_coldchain
from sections.insights import show_insights

# --- Header ---
st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a, #1e293b);
                padding: 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h1 style="color: #38bdf8; margin: 0;">🎯 Dashboard Estratégico CL Circular</h1>
        <p style="color: #94a3b8; margin: 0.5rem 0 0 0;">
            Análisis de Inteligencia de Negocios · Expansión México → USA · HS06/07/08
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Navegación en Sidebar ---
st.sidebar.image(
    "https://via.placeholder.com/200x60/0f172a/38bdf8?text=CL+Circular",
    use_column_width=True
)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Navegación")

seccion = st.sidebar.radio(
    label="",
    options=[
        "Executive Summary",
        "Market Overview",
        "Market Players",
        "Logistics Corridors",
        "Cold Chain & Compliance",
        "Strategic Insights"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Mercado:** México → USA")
st.sidebar.markdown("**Capítulos:** HS06 · HS07 · HS08")
st.sidebar.markdown("**Actualizado:** Marzo 2026")

# --- Enrutador de secciones ---
if seccion == " Executive Summary":
    show_executive()
elif seccion == " Market Overview":
    show_market()
elif seccion == " Market Players":
    show_players()
elif seccion == " Logistics Corridors":
    show_corridors()
elif seccion == " Cold Chain & Compliance":
    show_coldchain()
elif seccion == " Strategic Insights":
    show_insights()
