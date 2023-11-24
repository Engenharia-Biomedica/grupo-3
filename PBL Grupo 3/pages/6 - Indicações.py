# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:41:59 2023

@author: joaob
"""

import streamlit as st

# Dicionário de antibióticos e sintomas correspondentes

antibioticos_sintomas = {
    'Levofloxacina': [
        'Sinusite aguda', 'Pneumonia', 'Impetigo', 'Abscessos na pele', 'Furúnculo', 
        'Celulite bacteriana', 'Erisipela', 'Osteomielite', 'Infecções do trato urinário', 
        'Infecções intra-abdominais', 'Infecção generalizada ou sepse'
    ],
    'Ceftriaxona': [
        'Sepse', 'Meningite', 'Infecções abdominais', 'Infecções dos ossos ou articulações', 
        'Pneumonia', 'Infecções da pele, ossos, articulações e tecidos moles', 
        'Infecções renais e do trato urinário', 'Infecções respiratórias', 'Gonorreia'
    ],
    'Clindamicina': [
        'Infecção respiratório', 'Infecção da pele e de tecidos moles', 'Infecção abdominal'
    ],
    'Sulfametoxazol + Trimetoprim': [
        'Pneumonia', 'Infecção urinária', 'Cistite', 'Pielonefrite', 'Bronquite', 'Shigelose', 
        'Diarréia do viajante', 'Granuloma inguinal', 'Meningite', 'Toxoplasmose'
    ],
    'Cefuroxima/Sodium': [
        'Bronquite', 'Infecão urinária', 'Pneumonia', 'Faringite e amigdalite', 'Infecção grave', 
        'Meningite'
    ],
    'Cefepime': [
        'Infecções do trato respiratório', 'Pneumonia', 'Bronquite', 'Infecções do trato urinário', 
        'Infecções de pele', 'Infecções intra-abdominais', 'Infecções ginecológicas', 'Septicemia'
    ],
    'Fluconazol': [
        'Pé de atleta', 'Micoses'
    ],
    'Vancomicina': [
        'Infecções nos ossos', 'Pulmões', 'Pele', 'Músculos e coração', 'Pneumonia', 
        'Osteomielite', 'Endocardite'
    ],
    'Ofloxacina': [
        'Infecções respiratórias', 'Infecções abdominais', 'Infecções nas vias urinárias', 
        'Infecções nas vias genitais'
    ],
    'Micafungina': [
        'Candidíase invasiva', 'Candidíase esofágica', 'Profilaxia'
    ],
    'Voriconazol': [
        'Aspergilose invasiva', 'Candidemia', 'Candidíase esofágica'
    ],
    'Penicilina': [
        'Amigdalite', 'Sinusites', 'Escarlatina', 'Erisipela', 'Pneumonia leve', 
        'Infecções de ouvido', 'Prevenção de febre reumática', 'Prevenção de endocardite bacteriana'
    ],
    'Penicilina - Meningites': [
        'Amigdalite', 'Sinusites', 'Escarlatina', 'Erisipela', 'Pneumonia leve', 
        'Infecções de ouvido', 'Prevenção de febre reumática', 'Prevenção de endocardite bacteriana'
    ],
    'Anfotericina B': [
        'Candidíase disseminada', 'Septicemia fúngica', 'Criptococose', 'Blastomicose', 
        'Coccidiodomicose', 'Histoplamose', 'Mucormicose', 'Leishmaniose cutânea ou visceral', 
        'Zigomicose'
    ],
    'Eritromicina': [
        'Pneumonia', 'Coqueluche', 'Conjuntivite', 'Bronquite', 'Infecções de pele', 
        'Uretrite', 'Cervicite', 'Proctite', 'Enterocolite', 'Acne vulgar', 'Linfogranuloma venéreo'
    ],
    'Ciprofloxacina': [
        'Infecções oftalmológicas', 'Infecções respiratórias', 'Infecções genitais', 
        'Infecções urinárias', 'Infecções abdominais', 'Infecções da pele'
    ],
    'Penicilina - Outros Materiais': [
        'Amigdalite', 'Sinusites', 'Escarlatina', 'Erisipela', 'Pneumonia leve', 
        'Infecções de ouvido', 'Prevenção de febre reumática', 'Prevenção de endocardite bacteriana'
    ],
    'Oxacilina': [
        'Infecções oftalmológicas', 'Infecções respiratórias', 'Infecções genitais', 
        'Infecções urinárias', 'Infecções abdominais', 'Infecções da pele'
    ],
    'Meropenem': ['Infecção da pele e dos tecidos mortos','Infecção intra-abdominal','Meningite'],
    'Ceftazidima': ['Infecção por um germe','Infecção no Pulmão','Infecção no ouvido','Infecção no nariz','Infecção na garganta','Infecção sistema urinário','Infecção no abdome','Infecção na vesícula biliar','Infecção nos ossos e articulações','Meningite'],
    'Amicacina': ['Infecções graves', 'Infecções do trato respiratório'],
    'Imipenem': ['Infecções graves', 'Infecções do trato respiratório'],
    'Ceftriaxona - Meningites': ['Meningites bacterianas'],
    'Ceftriaxona - Outros Materiais': ['Infecções bacterianas'],
    'Penicilina - Oral': ['Infecções bacterianas'],
    'Ertapenem': ['Infecções graves', 'Infecções do trato respiratório'],
    'Gentamicina': ['Infecções graves', 'Infecções do trato urinário'],
    'Ampicilina/Sulbactam': ['Infecções bacterianas'],
    'Ceftarolina': ['Infecções bacterianas'],
    'Amoxacilina/Ac. Clavulânico': ['Infecções bacterianas'],
    'Piperacilina/Tazobactam': ['Infecções graves', 'Infecções do trato respiratório'],
    'Caspofungina': ['Candidíase invasiva', 'Candidíase esofágica'],
    'Teicoplanina': ['Infecções por MRSA', 'Infecções por estafilococos'],
    'Anidulafungina': ['Candidíase invasiva', 'Candidíase esofágica'],
    'Ampicilina': ['Infecções bacterianas'],
    'Cefazolina': ['Infecções bacterianas', 'Infecções do trato respiratório'],
    'Ceftazidima/avibactam': ['Infecções bacterianas', 'Pneumonia'],
    'Daptomicina': ['Infecções por MRSA', 'Infecções por estafilococos'],
    'Cefuroxima': ['Infecções do trato respiratório', 'Infecções da pele'],
    'Isavuconazol': ['Aspergilose invasiva', 'Candidemia', 'Candidíase esofágica'],
    'Polimixina B': ['Infecções graves', 'Infecções do trato urinário'],
    'Penicilina - Pneumonia': ['Pneumonia bacteriana'],
    'Itraconazol': ['Infecções fúngicas', 'Candidíase'],
    'Aztreonam': ['Infecções bacterianas', 'Infecções do trato respiratório'],
}


st.title('Seletor de Antibióticos')

# Seleção de sintomas
selected_symptoms = st.multiselect('Selecione os sintomas:', list(set([symptom for symptoms_list in antibioticos_sintomas.values() for symptom in symptoms_list])))

if selected_symptoms:
    selected_antibiotics = []
    for antibiotic, symptoms in antibioticos_sintomas.items():
        if any(symptom in symptoms for symptom in selected_symptoms):
            selected_antibiotics.append(antibiotic)

    st.subheader('Antibióticos sugeridos:')
    if selected_antibiotics:
        for antibiotic in selected_antibiotics:
            st.write(antibiotic)
    else:
        st.write('Nenhum antibiótico encontrado para os sintomas selecionados.')