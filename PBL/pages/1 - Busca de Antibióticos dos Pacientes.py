
import pandas as pd
import streamlit as st

db = pd.read_csv('pbl-tratado.csv', sep=',')

st.header("Painel de Monitoramento de Pacientes")

st.subheader('Tabela interativa de dados', divider='rainbow')

def select_box():
    microorganismo = st.selectbox(
        "Antibióticos: ",
        ['Todos'] + list(db["ds_antibiotico_microorganismo"].unique())
    )

    if microorganismo == 'Todos':
        db_filt = db
    else:
        db_filt = db[db["ds_antibiotico_microorganismo"] == microorganismo]

    resistencia = st.selectbox(
        "Interpretação do antibiótico: ",
        ['Todos'] + list(db_filt["cd_interpretacao_antibiograma"].unique())
    )
    
    if resistencia != 'Todos':
        db_filt = db_filt[db_filt["cd_interpretacao_antibiograma"] == resistencia]

    st.dataframe(db_filt)

select_box()

