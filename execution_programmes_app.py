# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:34:42 2024

@author: ok
"""

import streamlit as st
import pandas as pd

st.header(':rainbow[EXÉCUTION DES PROGRAMMES SCOLAIRES]:books:', anchor='CENTER')
st.subheader('Application développée par : Chabi Zimé GOUNOU N\'GOBI, Planificateur de l\'éducation, DataScientist')

# DataFrame global pour stocker les données de tous les collèges
global_df = pd.DataFrame(columns=['Commune', 'Nom du collège', 'Discipline', 'Promotion', 'Taux prévu', 'Taux d\'exécution minimum (%)', 'Taux d\'exécution maximum (%)'])

# Liste des communes
communes = ['Banikoara', 'Gogounou', 'Kandi', 'Karimama', 'Malanville', 'Ségbana']

st.subheader('1. Identification du collège')
# Sélection de la commune
commune_selected = st.selectbox('Sélectionnez la commune :', communes)

# Nom du collège
list_colleges = []

def choix_college():
    global list_colleges
    if commune_selected == 'Banikoara':
        list_colleges = ['CEG Arbonga', 'CEG Banikoara', 'CEG Founougo']
    elif commune_selected == 'Gogounou':
        list_colleges = ['CEG Bagou', 'CEG Gogounou','CEG Gounarou', 'CEG Sori', 'CEG Wara', 'CEG Zougou P.']
    elif commune_selected == 'Kandi':
        list_colleges = ['CEG 1 Kandi', 'CEG 2 Kandi','CEG 3 Kandi', 'CEG Angaradébou', 'CEG Bensékou', 'Donwari']
    elif commune_selected == 'Karimama':
        list_colleges = ['CEG Birni lafia', 'CEG Karimama','CEG Kompa']
    elif commune_selected == 'Malanville':
        list_colleges = ['CEG Garou', 'CEG Guéné','CEG Madécali','CEG Malanville', 'CEG Toumboutou', 'CEG Wollo']
    elif commune_selected == 'Ségbana':
        list_colleges = ['CEG libantè', 'CEG liboussou','CEG lougou','CEG Piami', 'CEG Ségbana', 'CEG Sokotindji']
    else:
        print('Sélectionnez votre commune!')

choix_college()
college_name = st.selectbox('Sélectionnez votre collège :', list_colleges)

# Cycle d'enseignement
cycle_enseignement = st.radio("Cycle d'enseignement :", ('1er cycle', '1er et 2nd cycles'))

# Définir les promotions en fonction du cycle d'enseignement
if cycle_enseignement == '1er cycle':
    promotions = ['6ième', '5ième', '4ième', '3ième']
else:
    promotions = ['6ième', '5ième', '4ième', '3ième', '2nd', '1ère', 'Tle']

st.subheader('2. Taux d\'exécution')

# Taux prévu
taux_prevu = st.number_input("Taux prévu (%)", min_value=0.0, max_value=100.0, step=0.5)

# Créer une section pour chaque discipline
disciplines = ['Mathématiques', 'Français', 'Histoire-Géographie', 'Sciences', 'Langues', 'Arts', 'EPS']

# DataFrame pour stocker les données du collège actuel
college_df = pd.DataFrame(columns=['Commune', 'Nom du collège', 'Discipline', 'Promotion', 'Taux prévu', 'Taux d\'exécution minimum (%)', 'Taux d\'exécution maximum (%)'])

# Initialisation du DataFrame
college_df = pd.DataFrame()

# Boucle sur les disciplines
for discipline in disciplines:
    st.subheader(discipline)
    
    # Diviser en 4 colonnes
    col1, col2, col3, col4 = st.columns(4)
    
    # Création des listes pour stocker les taux d'exécution min et max par promotion
    taux_min = {}
    taux_max = {}
    
    # Boucle sur les promotions
    for promotion in promotions:
        with col1:
            st.write("Taux prévu")
            st.write(taux_prevu)
        
        with col2:
            taux_min[promotion] = st.number_input(f"Taux minimum (%) {promotion}", min_value=0.0, max_value=100.0, step=0.5, key=f"min_{discipline}_{promotion}")
        
        with col3:
            taux_max[promotion] = st.number_input(f"Taux maximum (%) {promotion}", min_value=0.0, max_value=100.0, step=0.5, key=f"max_{discipline}_{promotion}")
        
        # Déterminer l'appréciation
        appreciation = "Bonne progression" if taux_min[promotion] >= taux_prevu else "Retard progression"
        with col4:
            st.write("Appréciation")
            if appreciation == "Bonne progression":
                st.write(appreciation, ":heavy_check_mark:")
            else:
                st.write(appreciation, ":x:")
        
    # Création du DataFrame pour la discipline en cours
    df = pd.DataFrame({
        'Commune': [commune_selected] * len(taux_min),
        'Nom du collège': [college_name] * len(taux_min),
        'Discipline': [discipline] * len(taux_min),
        'Promotion': list(taux_min.keys()),
        'Taux prévu': [taux_prevu] * len(taux_min),
        'Taux d\'exécution minimum (%)': list(taux_min.values()),
        'Taux d\'exécution maximum (%)': list(taux_max.values())
    })
    
    # Concaténation du DataFrame de la discipline en cours avec le DataFrame global
    college_df = pd.concat([college_df, df], ignore_index=True)

# Affichage du DataFrame global
st.write("Taux d'exécution réalisé par promotion :")
st.write(college_df)

















