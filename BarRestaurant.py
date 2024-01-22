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
        
    lab_heure = Label(root, text = '', font = ('Calibri light', 10, 'italic', 'bold'), fg='black', bg='sky blue')
    lab_heure.place (x=1, y=10)

    affich_heure()

    #Création de la zone de Frame,
    zone = Frame(root,bd=2, relief=GROOVE, bg='white')
    zone.place(x=15,y=50,width=1340, height=650)

    #Création de la zone client,
    zone_client = LabelFrame(zone, text='Client', font=('Calibri light',15, 'italic', 'bold'), bg='white')
    zone_client.place(x=10, y=10, width=400, height=150)
    #Contact_lient
    #contact_client = Label(zone_client, text = 'Contact :', font=('Calibri light',12, 'italic', 'bold'), bg='white')
    #contact_client.pack()






if __name__ == '__main__':
  root = Tk()
  obj = MonRestaurant(root)
  root.mainloop()
