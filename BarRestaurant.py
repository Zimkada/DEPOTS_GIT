# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:34:20 2024

@author: ok
"""

#Importation de tkinter et des autres modules
from tkinter import *
from tkinter import messagebox, ttk
import tempfile
import random
from time import strftime
from PIL import ImageTk, Image
import os

#Création de la classe MonRestaurant et de l'interface graphique
class MonRestaurant:
    
    def __init__(self,root):
      self.root = root
      self.root.title('BAR_RESTAURANT')
      self.root.geometry("1920x1040+0+0")
                         
      title = Label(root, text = 'MON BAR-RESTAURANT', font = ('Bookman Old style', 20, 'bold', 'italic', 'underline'), fg='black', bg='sky blue')
      title.pack(side=TOP, fill=X)
      
      #Affichage de l'heure
  
      def affich_heure():
          heure = strftime("%H:%M:%S")
          lab_heure.config(text=heure)
          lab_heure.after(1000,affich_heure)
          
      lab_heure = Label(root, text = '', font = ('Abadi', 12, 'italic', 'bold'), fg='black', bg='sky blue')
      lab_heure.place (x=1, y=10)

      affich_heure()

      #Déclaration des variables
      self.contact_client = IntVar()
      self.nom_client = StringVar()
      self.email_client = StringVar()
      self.qte_produit = IntVar()
      self.prix_unit = IntVar()
      self.prix_total = IntVar()
      self.produit = StringVar()
      self.sous_categorie = StringVar()
      self.total_brut = IntVar()
      self.taxe = IntVar()
      self.total_net = IntVar()
      
      self.rech_fac = IntVar() #A compléter fonction random
      
  
      #Définition des listes de sous_catégories, produits et prix Catégorie
      self.list_categorie = ['Rafraîchissement', 'Restaurant']
      
      #Ctégorie Bar:
      self.list_sous_cat_raf = ['Bière', 'Sucrerie', 'Liqueur', 'Vin']
      
      self.list_biere = ['Béninoise 30', 'Béninoise 60', 'Beaufort 30', 'Beaufort 50', 'Doppel', 'Guinsess', 'Castel', 'Flag']
      self.list_sucrerie = ['World cola 30', 'World cola 60', 'Youzou 30', 'Youzou 60', 'Youki Cocktail 30', 'Youki Cocktail 60', 'Youki Pamplemousse 30', 'Youki Pamplemousse 60']
      self.list_liqueur = ['William lawsons', 'Johnnie walker', 'Jack Daniels', 'Hennessy']
      self.list_vin = ['Révélation','Agor']
      
      self.prix_beninoise30 = 350
      self.prix_beninoise60 = 600
      self.prix_beaufort30 = 400
      self.prix_beaufort50 = 600
      self.prix_doppel = 650
      self.prix_guinness = 700
      self.prix_castel = 600
      self.prix_flag = 600
      
      self.prix_wordcola30 = 300
      self.prix_worldcola60 = 500
      self.prix_youzou30 = 300
      self.prix_youzou60 = 500
      self.prix_youkicock30 = 300
      self.prix_youkipamp30 = 300
      self.prix_youkicock60 = 500
      self.prix_youkipamp60 = 500
      
      self.prix_william = 10000
      self.prix_johnnie = 10000
      self.prix_jack = 12000
      self.prix_hennessy = 15000
      
      self.prix_revelation = 6000
      self.prix_agor = 6000
      
   
      
   
      #Création de la zone de Frame,
      zone = Frame(root,bd=2, relief=GROOVE, bg='white')
      zone.place(x=15,y=50,width=1340, height=650)
  
          #Création de la zone client
      zone_client = LabelFrame(zone, text='CLIENT', font=('Calibri light',15, 'italic', 'bold', 'underline'), bg='white')
      zone_client.place(x=10, y=10, width=300, height=120)
      
              #Contact_lient
      self.contact_client = Label(zone_client, text = 'Contact(s) :', font=('Calibri light',12, 'italic', 'bold'), bg='white')
      self.contact_client.grid(row=0, column=0, ipady = 1, sticky = 'w')
      self.text_contact_client = ttk.Entry(zone_client, text = self.contact_client, font = ('Calibri light',10, 'italic', 'bold'))
      self.text_contact_client.grid(row = 0, column = 1, ipady = 1, pady = 1)
      
              #nom du client
      self.nom_client = Label(zone_client, text = 'Nom du client :', font=('Calibri light',12, 'italic', 'bold'), bg='white')
      self.nom_client.grid(row = 1, column = 0, ipady = 1, sticky = 'w')
      self.text_nom_client = ttk.Entry(zone_client, text=self.nom_client, font=('Calibri light',10, 'italic', 'bold'))
      self.text_nom_client.grid(row = 1, column = 1, ipady = 1, pady = 1)
      
      
              #Email du client
      self.email_client = Label(zone_client, text = 'Email :', font=('Calibri light',12, 'italic', 'bold'), bg='white')
      self.email_client.grid(row = 2, column = 0, ipady = 1, sticky = 'w')
      self.text_email_client = ttk.Entry(zone_client, text=self.email_client, font=('Calibri light',10, 'italic', 'bold'))
      self.text_email_client.grid(row = 2, column = 1, ipady = 1, pady = 1)
      
          #Création de la zone produit
      zone_produit = LabelFrame(zone, text='PRODUIT', font=('Calibri light',15, 'italic', 'bold', 'underline'), bg='white')
      zone_produit.place(x=320, y=10, width=540, height=120)
      
              #Catégorie de produit
      self.categorie_produit = Label(zone_produit, text = 'Catégorie :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.categorie_produit.grid(row = 0, column = 0, sticky ='w', ipady = 1)
      
      self.text_categorie_produit = ttk.Combobox(zone_produit, values = self.list_categorie, font=('Calibri light',10, 'italic'))
      self.text_categorie_produit.grid(row = 0, column = 1, sticky = 'w', ipady = 1)
      self.text_categorie_produit.bind("<<ComboboxSelected>>", self.affectSousCat)

      
      
      
              #Sous-Catégorie de produit
      self.sous_categorie_produit = Label(zone_produit, text = 'Sous-catégorie :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.sous_categorie_produit.grid(row = 1, column = 0, sticky ='w', ipady = 1)
      
      self.text_sous_categorie_produit = ttk.Combobox(zone_produit, textvariable = self.sous_categorie, font=('Calibri light',10, 'italic'))
      self.text_sous_categorie_produit.grid(row = 1, column = 1, sticky = 'w', ipady = 1)
      self.text_sous_categorie_produit.bind('<<ComboboxSelected>>', self.affectNomProduit)
      
              #Nom des produits
      self.nom_produit = Label(zone_produit, text = 'Nom produit :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.nom_produit.grid(row = 2, column = 0, sticky ='w', ipady = 1)
      
      self.text_nom_produit = ttk.Combobox(zone_produit, textvariable = self.produit, font=('Calibri light',10, 'italic'))
      self.text_nom_produit.grid(row = 2, column = 1, sticky = 'w', ipady = 1)
      self.text_nom_produit.bind('<<ComboboxSelected>>', self.affectPrixProduit)
      
             #Quantité produit
      self.quantite_produit = Label(zone_produit, text = 'Quantité :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.quantite_produit.grid(row = 0, column = 2 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_qte_produit = ttk.Entry(zone_produit, textvariable = self.qte_produit, font=('Calibri light',10, 'italic'))
      self.text_qte_produit.grid(row = 0, column = 3, sticky = 'w', ipady = 1, pady = 1, ipadx = 8)
      
              #Prix_unit produit
      self.prix_unit_produit = Label(zone_produit, text = 'Prix/u :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.prix_unit_produit.grid(row = 1, column = 2 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_prix_unit_produit = ttk.Combobox(zone_produit, textvariable = self.prix_unit, font=('Calibri light',10, 'italic'), state = 'readonly')
      self.text_prix_unit_produit.grid(row = 1, column = 3, sticky = 'w', ipady = 1, pady = 1)
      #self.text_prix_unit_produit.bind('<<ComboboxSelected>>', self.affecttotalPrix)
      
             #prix total produit
      self.prix_total_produit = Label(zone_produit, text = 'Total :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.prix_total_produit.grid(row = 2, column = 2 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_prix_total_produit = ttk.Entry(zone_produit, text = self.prix_total, font=('Calibri light',10, 'italic'), state = 'readonly')
      self.text_prix_total_produit.grid(row = 2, column = 3, sticky = 'w', ipady = 1, pady = 1, ipadx = 8)
      
      #image
      self.img_bar = ImageTk.PhotoImage(Image.open('C:/Users/ok/PROJETS PYTHON/supermarket/plan-bar.jpg'))
      self.lbl_image = Label(image=self.img_bar)
      self.lbl_image.place(x=30, y=190, width=850, height=350)


      #Création de la sous zone de recherche de facture et ses widgets
      zone_recherche = LabelFrame(zone, text='RECHERCHE FACTURE', font=('Calibri light',15, 'italic', 'bold', 'underline'), bg='white')
      zone_recherche.place(x=880, y=10, width=400, height=120)
          
      self.recherche_fac = Label(zone_recherche, text = 'N° Facture :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.recherche_fac.grid(row = 0, column = 0 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_rech_fac = ttk.Entry(zone_recherche, textvariable = self.rech_fac, font=('Calibri light',10, 'italic'))
      self.text_rech_fac.grid(row = 0, column = 1, sticky = 'w', ipady = 1, pady = 1, ipadx = 8)
      
      
          #Bouton de recherche
      self.button_rech = Button(zone_recherche, text = 'Recherche', height=1, font=('Calibri light',10, 'italic', 'bold'),fg='black', bg='sky blue', cursor='hand2')
      self.button_rech.grid(row=0, column=2, sticky = '', ipady = 1, pady = 1, ipadx = 8)
      
      #Zone facture et ses widgets
      zone_facture = LabelFrame(zone, text=' FACTURE', font=('Calibri light',15, 'italic', 'bold', 'underline'), bg='white')
      zone_facture.place(x=880, y=150, width=450, height=480)
      
      scroll_y = Scrollbar(zone_facture, orient=VERTICAL)
      self.zone_text_facture = Text(zone_facture, yscrollcommand=scroll_y.set, font=('abadi',12, 'italic', 'bold'), bg='#D6EAF8', fg= 'black')
      scroll_y.pack(fill=Y, side=LEFT)
      scroll_y.configure(command=self.zone_text_facture.yview)
      self.zone_text_facture.pack(fill=BOTH, expand=1)
      
      #Zone des fonctions
      
      zone_fonctions = LabelFrame(zone, text=' FONCTIONS', font=('Calibri light',15, 'italic', 'bold', 'underline'), bg='#F4F6F7')
      zone_fonctions.place(x=10, y=500, width=850, height=130)
      
      self.lbl_total_brut = Label(zone_fonctions, text = 'Total brut :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.lbl_total_brut.grid(row = 0, column = 0 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_total_brut = ttk.Entry(zone_fonctions, textvariable = self.total_brut, font=('Calibri light',10, 'italic'), state='readonly')
      self.text_total_brut.grid(row = 0, column = 1, sticky = 'w', ipady = 1, pady = 1, ipadx = 8)
      
      self.lbl_taxe = Label(zone_fonctions, text = 'Taxe :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.lbl_taxe.grid(row = 1, column = 0 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_taxe = ttk.Entry(zone_fonctions, textvariable = self.taxe, font=('Calibri light',10, 'italic'), state='readonly')
      self.text_taxe.grid(row = 1, column = 1, sticky = 'w', ipady = 1, pady = 1, ipadx = 8)
      
      self.lbl_total_net = Label(zone_fonctions, text = 'Total net :', font=('Calibri light',11, 'italic', 'bold'), bg='white')
      self.lbl_total_net.grid(row = 2, column = 0 , sticky ='w', ipady = 1, pady = 1)
      
      self.text_total_net = ttk.Entry(zone_fonctions, textvariable = self.total_net, font=('Calibri light',10, 'italic'), state='readonly')
      self.text_total_net.grid(row = 2, column = 1, sticky = 'w', ipady = 1, pady = 1, ipadx = 8)
      
          #Bouton de recherche
      #self.button_rech = Button(zone_recherche, text = 'Recherche', height=1, font=('Calibri light',10, 'italic', 'bold'),fg='black', bg='sky blue', cursor='hand2')
      #self.button_rech.grid(row=0, column=2, sticky = '', ipady = 1, pady = 1, ipadx = 8)
      





#Fonction d'affection des sous-catégorie
    def affectSousCat(self, event = ''):
        if self.text_categorie_produit.get() == 'Rafraîchissement':
            return self.text_sous_categorie_produit.config(values = self.list_sous_cat_raf) 
    
    def affectNomProduit(self, event =''):
        if self.text_sous_categorie_produit.get() == 'Bière':
            return self.text_nom_produit.config(values = self.list_biere)
        if self.text_sous_categorie_produit.get() == 'Sucrerie':
            return self.text_nom_produit.config(values = self.list_sucrerie)
        if self.text_sous_categorie_produit.get() == 'Liqueur':
            return self.text_nom_produit.config(values = self.list_liqueur)
        if self.text_sous_categorie_produit.get() == 'Vin':
            return self.text_nom_produit.config(values = self.list_vin)
        
    def affectPrixProduit(self, event=''):
        #Bière ['Béninoise 30', 'Béninoise 60', 'Beaufort 30', 'Beaufort 50', 'Doppel', 'Guinsess', 'Castel', 'Flag']
        if self.text_nom_produit.get() == 'Béninoise 30':
            self.text_prix_unit_produit.config(values = self.prix_beninoise30)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Béninoise 60':
            self.text_prix_unit_produit.config(values = self.prix_beninoise60)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Beaufort 30':
            self.text_prix_unit_produit.config(values = self.prix_beaufort30)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        if self.text_nom_produit.get() == 'Beaufort 50':
            self.text_prix_unit_produit.config(values = self.prix_beaufort50)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        if self.text_nom_produit.get() == 'Doppel':
            self.text_prix_unit_produit.config(values = self.prix_doppel)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        if self.text_nom_produit.get() == 'Guinness':
            self.text_prix_unit_produit.config(values = self.prix_guinness)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        if self.text_nom_produit.get() == 'Castel':
            self.text_prix_unit_produit.config(values = self.prix_castel)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        if self.text_nom_produit.get() == 'Flag':
            self.text_prix_unit_produit.config(values = self.prix_flag)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
    
        #Sucreries ['World cola 30', 'World cola 60', 'Youzou 30', 'Youzou 60', 
        #'Youki Cocktail 30', 'Youki Cocktail 60', 'Youki Pamplemousse 30', 'Youki Pamplemousse 60']
        if self.text_nom_produit.get() == 'World cola 30':
            self.text_prix_unit_produit.config(values = self.prix_wordcola30)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'World cola 60':
            self.text_prix_unit_produit.config(values = self.prix_worldcola60)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Youzou 30':
            self.text_prix_unit_produit.config(values = self.prix_youzou30)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Youzou 60':
            self.text_prix_unit_produit.config(values = self.prix_youzou60)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Youki Cocktail 30':
            self.text_prix_unit_produit.config(values = self.prix_youkicock30)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Youki Cocktail 60':
            self.text_prix_unit_produit.config(values = self.prix_youkicock60)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Youki Pamplemousse 30':
            self.text_prix_unit_produit.config(values = self.prix_youkipamp30)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Youki Pamplemousse 60':
            self.text_prix_unit_produit.config(values = self.prix_youkipamp60)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        
        # Liqueur : ['William lawsons', 'Johnnie walker', 'Jack Daniels', 'Hennessy']
        if self.text_nom_produit.get() == 'William lawsons':
            self.text_prix_unit_produit.config(values = self.prix_william)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Johnnie walker':
            self.text_prix_unit_produit.config(values = self.prix_johnnie)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Jack Daniels':
            self.text_prix_unit_produit.config(values = self.prix_jack)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Hennessy':
            self.text_prix_unit_produit.config(values = self.prix_hennessy)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
        
        # Vin : ['Révélation','Agor']
        if self.text_nom_produit.get() == 'Révélation':
            self.text_prix_unit_produit.config(values = self.prix_revelation)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)
            
        if self.text_nom_produit.get() == 'Agor':
            self.text_prix_unit_produit.config(values = self.prix_agor)
            self.text_prix_unit_produit.current(0)
            self.qte_produit.set(1)





if __name__ == '__main__':
  root = Tk()
  obj = MonRestaurant(root)
  root.mainloop()
