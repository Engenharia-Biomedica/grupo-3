import pandas as pd
import streamlit as st

db = pd.read_csv('pbl-tratado.csv', sep=',')

st.header("Painel de Monitoramento de Pacientes")

st.subheader('Tabela interativa de dados', divider='rainbow')

def select_box():
    local = st.selectbox(
        "Local: ",
        ['Todos'] + list(db["ds_predio_coleta"].unique())
    )
    if local == 'Todos':
        db_filt = db
    else:
        db_filt = db[db["ds_predio_coleta"] == local]

    resistencia = st.selectbox(
        "Interpretação do antibiótico: ",
        ['Todos'] + list(db_filt["ds_micro_organismo"].unique())
    )
    
    if resistencia != 'Todos':
        db_filt = db_filt[db_filt["ds_micro_organismo"] == resistencia]

    st.dataframe(db_filt)

select_box()





