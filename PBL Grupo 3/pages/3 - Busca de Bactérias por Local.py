import pandas as pd
import streamlit as st

# Carregamento de dados - carrega os dados do arquivo excel
db = pd.read_csv('pbl.csv', sep=',')

# Header
st.header("Painel de Monitoramento de Pacientes")

# Subheader
st.subheader('Tabela interativa de dados', divider='rainbow')

#"ds_micro_organismo" ---> MOSTRA O MICROORGANISMO
#"ds_predio_coleta"

# Criando um filtro de dados para antibióticos
local = st.selectbox(
    "Local: ",
    ['Todos'] + list(db["ds_predio_coleta"].unique())
)

if local == 'Todos':

    db_filt = db

else:

    db_filt = db[db["ds_predio_coleta"] == local]


# Criando um filtro de dados para interpretação do antibiótico
resistencia = st.selectbox(
    "Microorganismo: ",
    ['Todos'] + list(db_filt["ds_micro_organismo"].unique())
)

if resistencia != 'Todos':

    db_filt = db_filt[db_filt["ds_micro_organismo"] == resistencia]


#carrega a tabela 

st.dataframe(db_filt)
