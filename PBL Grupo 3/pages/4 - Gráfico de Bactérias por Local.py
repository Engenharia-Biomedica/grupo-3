# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:53:33 2023

@author: joaob
"""

import pandas as pd
import streamlit as st

# Carregamento de dados
db = pd.read_csv('pbl.csv', sep=',')

# Header
st.header("Painel de Monitoramento de Bactérias em Cada Local")

# Subheader
st.subheader("Dados do período de 2017-2023", divider='rainbow')

# Criando um filtro de dados
predio_coleta = st.selectbox(
    "Local: ",
    ['Todos'] + list(db["ds_predio_coleta"].unique())
)

if predio_coleta == 'Todos':
    db_filt = db
    paleta_cor = "ds_predio_coleta"
else:
    db_filt = db[db["ds_predio_coleta"] == predio_coleta]
    paleta_cor = None


# Mostrando o gráfico para o usuário
st.line_chart(
    data = db_filt,
    x = "ds_micro_organismo", 
    y = "ds_predio_coleta", 
    color = paleta_cor
)

