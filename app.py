import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard de Fauna", layout="wide")

# Dados gerais do projeto
metricas_gerais = {
    "Campanhas realizadas": 20,
    "Campanhas previstas": 32,
    "Pontos amostrais": 54,
    "Espécies ameaçadas": 16,
    "Grupos monitorados": 4,
}

grupos_monitorados = [
    "Mastofauna",
    "Avifauna",
    "Herpetofauna",
    "Quiropterofauna",
]

# Indicadores ecológicos
indicadores_df = pd.DataFrame(
    {
        "Grupo": ["Mastofauna", "Avifauna", "Herpetofauna", "Quiropterofauna"],
        "Riqueza": [32, 84, 27, 19],
        "Diversidade": [2.78, 3.41, 2.21, 2.49],
        "Similaridade": [71, 76, 64, 69],
        "Espécies ameaçadas": [4, 7, 3, 2],
    }
)

resumos_tecnicos = {
    "Mastofauna": "Boa cobertura espacial e tendência de estabilização da curva de espécies.",
    "Avifauna": "Maior riqueza entre os grupos e forte relação com heterogeneidade de habitats.",
    "Herpetofauna": "Grupo sensível à sazonalidade, recomendado reforço em campanhas no período chuvoso.",
    "Quiropterofauna": "Importante para avaliação de conectividade ecológica e corredores ripários.",
}

st.title("Dashboard de Monitoramento de Fauna")
st.caption("Projeto de apoio a consultoria ambiental para clientes de licenciamento.")

aba_visao_geral, aba_indicadores, aba_resumo = st.tabs(
    ["Visão geral do projeto", "Indicadores ecológicos", "Resumo técnico"]
)

with aba_visao_geral:
    st.subheader("Indicadores principais")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Campanhas realizadas", metricas_gerais["Campanhas realizadas"])
    col2.metric("Campanhas previstas", metricas_gerais["Campanhas previstas"])
    col3.metric("Pontos amostrais", metricas_gerais["Pontos amostrais"])
    col4.metric("Espécies ameaçadas", metricas_gerais["Espécies ameaçadas"])
    col5.metric("Grupos monitorados", metricas_gerais["Grupos monitorados"])

    st.markdown("### Grupos monitorados")
    st.write(
        pd.DataFrame({"Grupo": grupos_monitorados})
    )

with aba_indicadores:
    st.subheader("Tabela de indicadores por grupo")
    st.dataframe(indicadores_df, use_container_width=True, hide_index=True)

    st.subheader("Riqueza por grupo")
    riqueza_por_grupo = indicadores_df.set_index("Grupo")["Riqueza"]
    st.bar_chart(riqueza_por_grupo, use_container_width=True)

with aba_resumo:
    st.subheader("Interpretação técnica por grupo")
    grupo_selecionado = st.selectbox("Selecione o grupo de fauna", grupos_monitorados)
    st.info(f"**{grupo_selecionado}:** {resumos_tecnicos[grupo_selecionado]}")
