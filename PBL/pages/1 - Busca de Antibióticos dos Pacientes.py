
import pandas as pd
import streamlit as st

#carrgeamento de dados buscando a fonte do arquivo .csv tratado 
db = pd.read_csv('pbl-tratado.csv', sep=',')

#header 
st.header("Painel de Monitoramento de Pacientes")

#subheader 
st.subheader('Tabela interativa de dados', divider='rainbow')

#criação de um filtro de dados 
def select_box():
    microorganismo = st.selectbox(
        "Antibióticos: ",
        ['Todos'] + list(db["ds_antibiotico_microorganismo"].unique()) #seleção da coluna específica do arquivo apenas com variáveis únicas 
    )

    #variável 'todos' irá retornas todos, else retorna apenas variáveis selecionadas 
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

    #filtro para remover as variáveis nulas 
    db_filt = db_filt.dropna(subset=["ds_antibiotico_microorganismo", "cd_interpretacao_antibiograma"])

    #retorno da tabela 
    st.dataframe(db_filt) 

select_box()

    st.dataframe(db_filt)

select_box()

