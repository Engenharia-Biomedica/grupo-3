import pandas as pd
import streamlit as st

# Carregamento de dados
db = pd.read_csv('pbl.csv', sep=',')

# Header
st.header("Painel de Monitoramento de Antibióticos")

# Subheader
st.subheader("Dados de uso de antibiótico no período de 2017-2023", divider='rainbow')

# Criando um filtro de dados
microorganismo = st.selectbox(
    "Microorganismos: ",
    ['Todos'] + list(db["ds_micro_organismo"].unique())
)

if microorganismo == 'Todos':
    db_filt = db
    paleta_cor = "ds_micro_organismo"
else:
    db_filt = db[db["ds_micro_organismo"] == microorganismo]
    paleta_cor = None

# Função para determinar a interpretação
def determinar_interpretacao(microorganismo, antibiotico):
    subset = db[(db['ds_micro_organismo'] == microorganismo) & 
                (db['ds_antibiotico_microorganismo'] == antibiotico)]
    if not subset.empty:
        return subset['cd_interpretacao_antibiograma'].iloc[0]
    else:
        return "Informação não encontrada"

# Mostrando o gráfico para o usuário
if microorganismo != 'Todos':
    antibioticos_disponiveis = db_filt[db_filt['ds_micro_organismo'] == microorganismo]['ds_antibiotico_microorganismo'].unique()
    antibiotico = st.selectbox(
        f"Antibióticos para {microorganismo}: ",
        ['Selecione'] + list(antibioticos_disponiveis)
    )
    if antibiotico != 'Selecione':
        interpretacao = determinar_interpretacao(microorganismo, antibiotico)
        st.write(f"Para o microorganismo {microorganismo} e o antibiótico {antibiotico}, a interpretação é: {interpretacao}")
        

# Mostrando o gráfico para o usuário
st.bar_chart(
    data = db,
    x = "cd_sigla_microorganismo", 
    y = "ds_antibiotico_microorganismo", 
    color = "cd_interpretacao_antibiograma"
    , width=0, height=0, use_container_width=True)
