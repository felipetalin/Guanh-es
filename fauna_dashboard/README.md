# Fauna Dashboard

Dashboard em Streamlit para apresentação de indicadores ecológicos em projetos de monitoramento de fauna voltados à consultoria ambiental.

## Estrutura

```text
fauna_dashboard/
├── app.py
├── requirements.txt
└── README.md
```

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Funcionalidades

- **Visão geral do projeto** com métricas em `st.metric`:
  - Campanhas realizadas
  - Campanhas previstas
  - Pontos amostrais
  - Espécies ameaçadas
  - Grupos monitorados
- **Indicadores ecológicos**:
  - Tabela com riqueza, diversidade, similaridade e espécies ameaçadas
  - Gráfico de barras de riqueza por grupo
- **Resumo técnico**:
  - Dropdown para seleção de grupo
  - Exibição de interpretação técnica do grupo selecionado

## Tecnologias

- Python
- Streamlit
- Pandas
