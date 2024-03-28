# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:33:42 2024

@author: ok
"""



#Importation des modules
import pandas as pd
#import numpy as np
import streamlit as st
import plotly.express as px

# Définir la couleur de fond de la page
st.set_page_config(page_title="Résultats scolaires", page_icon="📚", layout="wide", initial_sidebar_state="expanded")

st.header(':rainbow[RÉSULTATS DU 1er TRIMESTRE DES COLLEGES PRIVÉS DE L\'ALIBORI]:books:', anchor='CENTER')
st.subheader(':orange[Application web développée par : Chabi Zimé GOUNOU N\'GOBI, Planificateur, DataScientist]:computer:')

#Chargement des données
df = pd.read_csv("prives_t1.csv",sep=";")

#Informations sur le jeu de données
#print(df.shape)
#print(df.describe())
#print(df.dtypes)



#Nettoyage du jeu de données
df.drop(['Unnamed: 36','Unnamed: 37','Unnamed: 38','Unnamed: 39'], 
        axis = 1, inplace = True)#Suppression des colonnes sans données
print(df.shape)


#Création des colonnes de moyennes supérieures à 10 et 12
df['Moyennes_sup_10 (%)'] = df['10_12_T'] + df['12_14_T'] + df['14_16_T'] + df['sup_16_T']
df['Moyennes_sup_12 (%)'] = df['12_14_T'] + df['14_16_T'] + df['sup_16_T']

st.title(':grey[1. Sélection d\'un collège]')

#Séléction du collège dont les résultats serot affichés
colleges = df.COLLEGES.unique()
college_selected = st.selectbox(':orange[Sélectionnez le collège :]', colleges, key="college_select")

selected_df = df[df['COLLEGES'] == college_selected]

st.title(f':grey[2. Résumé des résultats de/du {college_selected}]')


show_df = selected_df[['COLLEGES',
                       'CLASSES',
                       'EFF_T',
                       'inf_6.5_T',
                       '6.5_7.5_T',
                       'Moyennes_sup_10 (%)',
                       'Moyennes_sup_12 (%)',
                       'sup_16_T',
                       'MOY_MAX_F',
                       'MOY_MAX_G']]

show_df.rename(columns={'EFF_T':'Effectifs',
                        'COLLEGES':'Collège',
                        'CLASSES':'Classes',
                        'inf_6.5_T':'Moyennes_inf_6.5 (%)', 
                        '6.5_7.5_T':'Moyennes_6.5_à_7.5 (%)',
                        'sup_16_T' : 'Moyennes_sup_16 (%)',
                        'MOY_MAX_F':'Forte_moy_F',
                        'MOY_MAX_G':'Forte_moy_G'}, 
               inplace = True)

st.write(':orange[Moyennes_inf_6.5 (%) : Pourcentage de moyennes strictement inférieures à 6,5]')
st.write(':orange[Moyennes_6.5_à_7.5 (%) : Pourcentage de moyennes comprises entre 6,5 et 7,5]')
st.write(':orange[Moyennes_sup_10 (%) : Pourcentage de moyennes supérieures ou égales à 10]')
st.write(':orange[Moyennes_sup_12 (%) : Pourcentage de moyennes supérieures ou égales à 12]')
st.write(':orange[Moyennes_sup_16 (%) : Pourcentage de moyennes supérieures ou égales à 16]')
st.write(':orange[Forte_moy_F : Plus forte Moyenne des élèves filles]')
st.write(':orange[Forte_moy_G : Plus forte Moyenne des élèves garçons]')

st.dataframe(show_df)

st.title(f':grey[3. Visualisation des résultats du {college_selected}]')
#Visualisation des pourcentages de moyennes par classe

label = ['Moyennes inférieures à 6.5', 
         'Moyennes entre 6.5 et 7.5', 
         'Moyennes entre 7.5 et 9', 
         'Moyennes entre 9 et 10', 
         'Moyennes entre 10 et 12',
         'Moyennes entre 12 et 14',
         'Moyennes entre 14 et 16',
         'Moyennes supérieures à 16']

if college_selected:
    for n in range(selected_df['CLASSES'].size):
        st.subheader(f"Classe /Cyle : " + selected_df['CLASSES'].iloc[n])
        col_T, col_F, col_G = st.columns(3)
        with col_T:
            st.write('Élèves garçons et filles')
            data_values_T = [selected_df['inf_6.5_T'].iloc[n], 
                           selected_df['6.5_7.5_T'].iloc[n], 
                           selected_df['7.5_9_T'].iloc[n], 
                           selected_df['9_10_T'].iloc[n],
                           selected_df['10_12_T'].iloc[n],
                           selected_df['12_14_T'].iloc[n],
                           selected_df['14_16_T'].iloc[n],
                           selected_df['sup_16_T'].iloc[n]]
            fig = px.pie(names = label, values = data_values_T, hole = 0.3)
            st.plotly_chart(fig,use_container_width=True)
        
        with col_F:
            st.write('Élèves filles uniquement')
            data_values_F = [selected_df['inf_6.5_F'].iloc[n], 
                           selected_df['6.5_7.5_F'].iloc[n], 
                           selected_df['7.5_9_F'].iloc[n], 
                           selected_df['9_10_F'].iloc[n],
                           selected_df['10_12_F'].iloc[n],
                           selected_df['12_14_F'].iloc[n],
                           selected_df['14_16_F'].iloc[n],
                           selected_df['sup_16_F'].iloc[n]]
            fig = px.pie(names = label, values = data_values_F, hole = 0.3)
            st.plotly_chart(fig,use_container_width=True)

        with col_G:
            
            st.write('Élèves garçons uniquement')
            data_values_G = [selected_df['inf_6.5_G'].iloc[0], 
                           selected_df['6.5_7.5_G'].iloc[0], 
                           selected_df['7.5_9_G'].iloc[0], 
                           selected_df['9_10_G'].iloc[0],
                           selected_df['10_12_G'].iloc[0],
                           selected_df['12_14_G'].iloc[0],
                           selected_df['14_16_G'].iloc[0],
                           selected_df['sup_16_G'].iloc[0]]
            
            fig = px.pie(names = label, values = data_values_G, hole = 0.3)
            #fig.show()
            st.plotly_chart(fig,use_container_width=True)