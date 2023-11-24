import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json
import requests 

# Carregamento de dados - carrega os dados do arquivo excel
db = pd.read_csv('antibioticos.csv', sep=',')

# Header
st.header("Antibióticos Relacionado a Sintomas", divider='rainbow')


# Criando um filtro de dados para antibióticos
local = st.selectbox(
    "Antibióticos: ",
    ['Todos'] + list(db["Antibióticos"].unique())
)

if local != 'Todos':
    db_filt = db[db["Antibióticos"] == local]
    tratamento_info = db_filt['Tratamento de:'].iloc[0]  # Obtém a informação de tratamento
    st.write(f"Informações sobre '{local}':")
    st.write(f"Indicado para: {tratamento_info}")

    
#Carregando imagem do site lottie - IMAGEM GRÁTIS
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottiefile("coding2.json")
lottie_hello = load_lottieurl("https://lottie.host/664fea3e-4357-41ad-b510-1520f9b409d5/WZFaJKAO4K.json")

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=None,
    width=None,
    key=None
    )


