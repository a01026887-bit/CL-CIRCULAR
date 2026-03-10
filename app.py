import streamlit as st

# --- Configuración de página ---
st.set_page_config(
    page_title="CL Circular – Estrategia de expansión",
    layout="wide",
    initial_sidebar_state="expanded"
)

# >>> PEGA AQUÍ ESTE BLOQUE <<<

st.markdown(
    """
    <style>
    /* Reducir ancho del sidebar y hacerlo tipo tarjeta flotante */
    section[data-testid="stSidebar"] {
        background-color: transparent !important;
    }

    /* Contenedor interno del sidebar */
    section[data-testid="stSidebar"] > div {
        background-color: #F9FAFB !important;
        border-radius: 16px;
        margin: 1.5rem 0.75rem;
        padding: 1.25rem 1rem 1.5rem 1rem;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.08);
    }

    /* Texto del sidebar */
    section[data-testid="stSidebar"] * {
        color: #111827 !important;
        font-size: 0.90rem;
    }

    /* Título "Navegación" un poco más sobrio */
    section[data-testid="stSidebar"] h3 {
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: #6B7280 !important;
    }

    /* Radio buttons más compactos */
    div[role="radiogroup"] > label {
        padding-top: 0.25rem;
        padding-bottom: 0.25rem;
    }

    /* Contenedor principal con menos padding lateral */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Importar secciones ---
from sections.executive import show_executive
from sections.market_overview import show_market
from sections.market_players import show_players
from sections.corridors import show_corridors
from sections.coldchain import show_coldchain


# --- Header ---
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #0f172a, #1e293b);
                padding: 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h1 style="color: #38bdf8; margin: 0;">Estrategia - CL Circular</h1>
        <p style="color: #94a3b8; margin: 0.5rem 0 0 0;">
            Análisis de Expansión · México → USA · Frutas/Flores/Verduras
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Navegación en Sidebar ---
# Logo CL Circular en la parte superior del sidebar
st.sidebar.image(
    "logo_cl_circular.png",
    use_column_width=True
)

st.sidebar.markdown("---")
st.sidebar.markdown("### NAVEGACIÓN")


seccion = st.sidebar.radio(
    label="",
    options=[
        " Executive Summary",
        " Market Overview",
        " Market Players",
        " Logistics Corridors",
        " Cold Chain & Compliance",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Mercado:** México → USA")
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
