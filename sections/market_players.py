import streamlit as st
import pandas as pd

def show_players():
    st.header("Market Players")

    # --- Dataset ---
    data = [
        ["APEAM", "Exportador", "Aguacate", "HS08", "Michoacán, MX", "29,000 productores, 90 empaques cert.", "Trazabilidad USDA/SENASICA"],
        ["Mission Produce", "Exportador", "Aguacate", "HS08", "Michoacán MX / CA USA", "#1 exportador MX, 65K acres", "Temp control 2 días Uruapan→Laredo"],
        ["Driscoll's Network", "Distribuidor", "Berries", "HS08", "Jalisco MX + Global", "900+ growers, 33% mercado USA ($6B)", "Research stations MX, innovación"],
        ["CAADES Sinaloa", "Exportador", "Tomate", "HS07", "Culiacán, Sinaloa", "40 productores high-tech, 25,584 ha", "Cluster drip irrigation + Nogales AZ"],
        ["Sysco Corporation", "Importador", "Produce diverso", "HS07/HS08", "Houston, TX", "#1 foodservice mundial, 76K empleados", "FreshPoint, flota temp-controlled"],
        ["US Foods", "Importador", "Produce diverso", "HS07/HS08", "Rosemont, IL", "#2 foodservice USA", "Logística temp-controlled"],
        ["Fresh Del Monte", "Importador", "Frutas", "HS08", "Coral Gables, FL", "Líder mundial integrado, 80+ países", "Supply chain global fresh produce"],
        ["West Pak Avocado", "Importador", "Aguacate", "HS08", "California, USA", "65K+ acres, 1,000+ growers", "Just Ripe services, value-added"],
        ["Calavo Growers", "Importador", "Aguacate", "HS08", "California, USA", "Major USA avocado marketer", "Cold chain origen→processing→retail"],
        ["EMEX", "Exportador", "Mango", "HS08", "Sinaloa/Nayarit/Jalisco", "415K ton/año, $530M USD", "Zona fly-free Sinaloa"],
        ["Bloom Farms", "Exportador", "Berries", "HS08", "Tala, Jalisco", "4M kg/temporada, 3,057 empleos", "Cooling especializado"],
        ["FD Berries", "Exportador", "Berries", "HS08", "Gómez Farías, Jalisco", "350+ ha, 1 container/día", "Cold chain compliance"],
        ["Mastronardi Produce", "Exportador", "Tomate", "HS07", "Operaciones MX + Laredo TX", "185K sq ft logistics Laredo", "Cold storage state-of-the-art"],
        ["E. Armata Inc.", "Distribuidor", "Produce diverso", "HS07/HS08", "Bronx NY (Hunts Point)", "60K sq ft temp-controlled", "RF tracking, iPad QC USDA-trained"],
    ]

    df = pd.DataFrame(data, columns=[
        "Empresa", "Rol", "Producto", "HS", "Ubicación", "Evidencia de Escala", "Cold Chain / Tech"
    ])

    # --- Filtros ---
    col1, col2, col3 = st.columns(3)
    filtro_hs   = col1.selectbox("Filtrar por HS", ["Todos", "HS08", "HS07", "HS06"])
    filtro_rol  = col2.selectbox("Filtrar por Rol", ["Todos", "Exportador", "Importador", "Distribuidor"])
    filtro_prod = col3.selectbox("Filtrar por Producto", ["Todos", "Aguacate", "Tomate", "Berries", "Mango", "Pimientos"])

    df_f = df.copy()
    if filtro_hs   != "Todos": df_f = df_f[df_f["HS"].str.contains(filtro_hs)]
    if filtro_rol  != "Todos": df_f = df_f[df_f["Rol"] == filtro_rol]
    if filtro_prod != "Todos": df_f = df_f[df_f["Producto"].str.contains(filtro_prod)]

    st.dataframe(df_f, use_container_width=True, hide_index=True)
    st.caption(f"Mostrando {len(df_f)} de {len(df)} empresas")
