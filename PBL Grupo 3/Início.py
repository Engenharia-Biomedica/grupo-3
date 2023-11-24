import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json
import requests 

# Header e Subheader - fazem o título e o subtítulo
st.header("Painel de Monitoramento de Antibióticos")
st.subheader('Dados Interativos de antibióticos no período de 2017-2023', divider='rainbow')
st.markdown("Projeto engenharia biomédica - Grupo 3")

# carregando imagem para o logo
img = Image.open("imagem-logo.png")

# dividindo o espaçamento da tela em colunas
left_col, cent_col, last_col, center_left, right_col = st.columns(5) 
# colocando o logo na coluna central
with cent_col:
    st.image(img, width=500)

#Carregando imagem do site lottie - IMAGEM GRÁTIS
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottiefile("coding.json")
lottie_hello = load_lottieurl("https://lottie.host/3cf2308c-97bc-46e3-90a8-96bef39a4e2b/lq9hcfdTbw.json")

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




