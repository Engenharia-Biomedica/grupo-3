import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json
import requests 

# Carregamento de dados - carrega os dados do arquivo excel
#db = pd.read_csv('pbl-tratado.csv', sep=',')

db = pd.read_csv('pbl.csv', sep=',')

# Header
st.header("Painel de Monitoramento de Pacientes")

# Subheader
st.subheader('Tabela interativa de dados', divider='rainbow')


#"ds_micro_organismo" ---> MOSTRA O MICROORGANISMO
#cd_sigla_microorganismo
#cd_sigla_antibiotico


#ds_antibiotico_microorganismo ---> MOSTRA O ANTIBIÓTICO
#"cd_interpretacao_antibiograma" ---> MOSTRA SE É SENSIVEL - Sensível / Resistente


# Criando um filtro de dados para antibióticos
microorganismo = st.selectbox(
    "Antibióticos: ",
    ['Todos'] + list(db["ds_antibiotico_microorganismo"].unique())
)

if microorganismo == 'Todos':

    db_filt = db

else:

    db_filt = db[db["ds_antibiotico_microorganismo"] == microorganismo]


# Criando um filtro de dados para interpretação do antibiótico
resistencia = st.selectbox(
    "Interpretação do antibiótico: ",
    ['Todos'] + list(db_filt["cd_interpretacao_antibiograma"].unique())
)

if resistencia != 'Todos':

    db_filt = db_filt[db_filt["cd_interpretacao_antibiograma"] == resistencia]

st.dataframe(db_filt)
