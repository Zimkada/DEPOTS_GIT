# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:34:42 2024

@author: ok
"""
import streamlit as st
import pandas as pd

# Définir les taux prévus par mois
taux_prevus_par_mois = {
    'Septembre': 10.00,
    'Octobre': 25.00,
    'Novembre': 35.00,
    'Décembre': 40.00,
    'Janvier': 60.00,
    'Février': 75.00,
    'Mars': 90.00,
    'Avril': 100.00,
    'Juin': 100.00
}

def renseigner_taux_execution():
    st.header(':rainbow[EXÉCUTION DES PROGRAMMES SCOLAIRES]:books:', anchor='CENTER')
    st.subheader('Application développée par : Chabi Zimé GOUNOU N\'GOBI, Planificateur de l\'éducation, DataScientist')

    st.subheader('1. Informations générales')

    # Liste des communes
    communes = ['Banikoara', 'Gogounou', 'Kandi', 'Karimama', 'Malanville', 'Ségbana']
    commune_selected = st.selectbox('Sélectionnez la commune :', communes, key="commune_select")

    # Nom du collège
    list_colleges = choix_college(commune_selected)
    college_name = st.selectbox('Sélectionnez votre collège :', list_colleges, key="college_select")

    # Cycle d'enseignement
    cycle_enseignement = st.radio("Cycle d'enseignement :", ('1er cycle', '1er et 2nd cycles'))

    st.subheader('2. Taux d\'exécution')

    # Option de choix du mois
    mois_selected = st.selectbox("Sélectionnez le mois :", list(taux_prevus_par_mois.keys()), key="mois_select")

    # Déterminer les promotions en fonction du cycle d'enseignement
    if cycle_enseignement == '1er cycle':
        promotions = ['6ième', '5ième', '4ième', '3ième']
    else:
        promotions = ['6ième', '5ième', '4ième', '3ième', '2nd', '1ère', 'Tle']

    # Déterminer le taux prévu en fonction du mois sélectionné
    taux_prevu = taux_prevus_par_mois.get(mois_selected)

    # Créer une section pour chaque discipline
    disciplines = ['Français', 'Anglais', 'Histoire-Géographie', 'Allemand', 'Espagnol', 'Philo', 'Mathématiques', 'PCT', 'SVT','EPS', 'Économie']

    # DataFrame pour stocker les données du collège actuel
    college_df = pd.DataFrame(columns=['Commune', 'Nom du collège', 'Discipline', 'Promotion', 'Taux prévu (%)', 'Taux minimum (%)', 'Taux maximum (%)'])

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
                st.write("Taux prévu (%)")
                st.write(taux_prevu)

            with col2:
                taux_min[promotion] = st.number_input(f"Taux minimum (%) {promotion}", min_value=0.0, max_value=100.0, step=0.5, key=f"min_{discipline}_{promotion}")

            with col3:
                taux_max[promotion] = st.number_input(f"Taux maximum (%) {promotion}", min_value=0.0, max_value=100.0, step=0.5, key=f"max_{discipline}_{promotion}")

            # Déterminer l'appréciation
            appreciation = "Bonne progression" if taux_min[promotion] >= taux_prevu else "Retard"
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
            'Taux prévu (%)': [taux_prevu] * len(taux_min),
            'Taux minimum (%)': list(taux_min.values()),
            'Taux maximum (%)': list(taux_max.values()),
            'Mois': [mois_selected] * len(taux_min)  # Ajout de la colonne 'Mois'
        })

        # Concaténation du DataFrame de la discipline en cours avec le DataFrame global
        college_df = df if college_df.empty else pd.concat([college_df, df], ignore_index=True)

    # Affichage du DataFrame global
    st.write("Taux d'exécution réalisé par promotion :")
    st.write(college_df)

    if st.button("Valider mes données"):
        # Récupérer les données stockées dans st.session_state
        global_df = st.session_state.get('global_df', pd.DataFrame(columns=['Commune', 'Nom du collège', 'Discipline', 'Promotion', 'Taux prévu', 'Taux d\'exécution minimum (%)', 'Taux d\'exécution maximum (%)', 'Mois']))
        # Ajouter les données validées au DataFrame global
        global_df = pd.concat([global_df, college_df], ignore_index=True)
        st.session_state['global_df'] = global_df  # Mettre à jour les données dans st.session_state
        st.success("Données validées avec succès !")

def modifier_taux_execution():
    st.header(':rainbow[EXÉCUTION DES PROGRAMMES SCOLAIRES]:books:', anchor='CENTER')
    st.header('Modifier mes taux d\'exécution')

    global_df = st.session_state.get('global_df', pd.DataFrame(columns=['Commune', 'Nom du collège', 'Discipline', 'Promotion', 'Taux prévu', 'Taux d\'exécution minimum (%)', 'Taux d\'exécution maximum (%)', 'Mois']))

    # Liste des communes
    communes = ['Banikoara', 'Gogounou', 'Kandi', 'Karimama', 'Malanville', 'Ségbana']
    selected_commune = st.selectbox("Sélectionner une commune :", communes)

    # Liste des collèges en fonction de la commune sélectionnée
    colleges = choix_college(selected_commune)
    selected_college = st.selectbox("Sélectionner un collège :", colleges)

    # Option de choix du mois pour filtrer les données
    mois_selected = st.selectbox("Sélectionnez le mois :", list(taux_prevus_par_mois.keys()), key="mois_select")

    # Filtrer les données en fonction de la commune, du collège sélectionné et du mois sélectionné
    filtered_data = global_df[(global_df['Commune'] == selected_commune) & (global_df['Nom du collège'] == selected_college) & (global_df['Mois'] == mois_selected)]

    # Si aucune donnée n'a été saisie pour ce collège et ce mois
    if filtered_data.empty:
        st.warning(f"Aucune donnée à modifier pour le collège {selected_college} pour le mois de {mois_selected}. Veuillez renseigner d'abord ces données au menu 'Renseigner les données'.")

    else:
        # Afficher les données à modifier
        st.write("Données à modifier :")
        st.write(filtered_data)

        # Modifier les taux d'exécution minimum et maximum
        for discipline in filtered_data['Discipline'].unique():
            st.subheader(discipline)

            # Diviser en 4 colonnes
            col1, col2, col3, col4 = st.columns(4)

            discipline_data = filtered_data[filtered_data['Discipline'] == discipline]
            for index, row in discipline_data.iterrows():
                key_min = f"new_min_{row['Discipline']}_{row['Promotion']}"
                key_max = f"new_max_{row['Discipline']}_{row['Promotion']}"
                new_min_value = st.number_input(f"Nouveau taux minimum (%) pour {row['Promotion']}", min_value=0.0, max_value=100.0, step=0.5, value=row['Taux d\'exécution minimum (%)'], key=key_min)
                new_max_value = st.number_input(f"Nouveau taux maximum (%) pour {row['Promotion']}", min_value=0.0, max_value=100.0, step=0.5, value=row['Taux d\'exécution maximum (%)'], key=key_max)

                # Mise à jour des données modifiées
                filtered_data.at[index, 'Taux minimum (%)'] = new_min_value
                filtered_data.at[index, 'Taux maximum (%)'] = new_max_value

        if st.button("Valider la modification de mes données"):
            # Mettre à jour les données modifiées dans le DataFrame global
            global_df.update(filtered_data)
            st.session_state['global_df'] = global_df  # Mettre à jour les données dans st.session_state
            st.success("Données modifiées avec succès !")

def visualiser_taux_execution():
    st.header(':rainbow[EXÉCUTION DES PROGRAMMES SCOLAIRES]:books:', anchor='CENTER')
    st.header('Visualiser mes taux d\'exécution')

    global_df = st.session_state.get('global_df', pd.DataFrame(columns=['Commune', 'Nom du collège', 'Discipline', 'Promotion', 'Taux prévu', 'Taux minimum (%)', 'Taux maximum (%)', 'Mois']))

    # Liste des communes
    communes = ['Banikoara', 'Gogounou', 'Kandi', 'Karimama', 'Malanville', 'Ségbana']
    selected_commune = st.selectbox("Sélectionner une commune :", communes)

    # Liste des collèges en fonction de la commune sélectionnée
    colleges = choix_college(selected_commune)
    selected_college = st.selectbox("Sélectionner un collège :", colleges)

    # Option de choix du mois pour filtrer les données
    mois_selected = st.selectbox("Sélectionnez le mois :", list(taux_prevus_par_mois.keys()), key="mois_select")

    # Filtrer les données en fonction de la commune, du collège sélectionné et du mois sélectionné
    filtered_data = global_df[(global_df['Commune'] == selected_commune) & (global_df['Nom du collège'] == selected_college) & (global_df['Mois'] == mois_selected)]

    # Filtrer les données validées
    validated_data = filtered_data.dropna()

    # Afficher les données
    st.write(validated_data)

def choix_college(commune_selected):
    list_colleges = []
    if commune_selected == 'Banikoara':
        list_colleges = ['CEG Arbonga', 'CEG Banikoara', 'CEG Founougo', 'CEG Gakounrou', 'CEG Gbassa', 'Gomparou', 
                         'CEG Goumori', 'CEG Kokey', 'CEG Kokiborou', 'CEG Ounet', 'CEG Sompérékou', 'CEG Soroko', 'CEG Toura']
    elif commune_selected == 'Gogounou':
        list_colleges = ['CEG Bagou', 'CEG Gogounou', 'CEG Gounarou', 'CEG Sori', 'CEG Wara', 'CEG Zougou P.']
    elif commune_selected == 'Kandi':
        list_colleges = ['CEG 1 Kandi', 'CEG 2 Kandi', 'CEG 3 Kandi', 'CEG Angaradébou', 'CEG Bensékou', 'Donwari', 
                         'CEG Kassakou', 'CEG Madina', 'CEG Pèdè', 'CEG Sam', 'CEG Sonsoro', 'CEG Tissarou']
    elif commune_selected == 'Karimama':
        list_colleges = ['CEG Birni lafia', 'CEG Karimama', 'CEG Kompa']
    elif commune_selected == 'Malanville':
        list_colleges = ['CEG Garou', 'CEG Guéné', 'CEG Madécali', 'CEG Malanville', 'CEG Toumboutou', 'CEG Wollo']
    elif commune_selected == 'Ségbana':
        list_colleges = ['CEG libantè', 'CEG liboussou', 'CEG lougou', 'CEG Piami', 'CEG Ségbana', 'CEG Sokotindji']
    else:
        print('Sélectionnez votre commune!')
    return list_colleges

def main():
    st.sidebar.title('MENUS')
    page = st.sidebar.radio("Aller à", ('Renseigner les taux d\'exécution', 'Modifier mes taux d\'exécution', 'Visualiser mes taux d\'exécution'))

    if page == 'Renseigner les taux d\'exécution':
        renseigner_taux_execution()
    elif page == 'Modifier mes taux d\'exécution':
        modifier_taux_execution()
    elif page == 'Visualiser mes taux d\'exécution':
        visualiser_taux_execution()

if __name__ == "__main__":
    main()
















    

















