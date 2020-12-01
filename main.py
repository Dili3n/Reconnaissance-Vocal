# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:23:15 2020

@author: xarfy
"""

from speech_recognition import Recognizer, Microphone
from random import *
from fltk import *
from gtts import gTTS 
from playsound import playsound

language = 'fr'

boucle = True 

text = str()

def calcul(x):
    
    mots = text.split(" ")
    if text.count(" ") == 2:
        var1 = mots[0]
        var2 = mots[2]
    
    if x == 0:
        resultat = int(var1) * int(var2)
        texte(200,500,("Resultat",str(resultat)))
        
    elif x == 1:
        resultat = int(var1) + int(var2)
        texte(200,500,("Resultat",str(resultat)))
    
    elif x == 2:
        resultat = int(var1) - int(var2)
        texte(200,500,("Resultat",str(resultat)))

def reconnaissance():
    
    with Microphone() as source:
        image(300,300,'assets/attendez.png', ancrage = "center")
        mise_a_jour()
        recognizer.adjust_for_ambient_noise(source)
        image(300,300,'assets/parlez.png', ancrage = "center")
        mise_a_jour()
        recorded_audio = recognizer.listen(source)
        image(300,300,'assets/bg.png', ancrage = "center")
        mise_a_jour()
        
    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="fr-FR"
            )
        print("Vous avez dit : {}".format(text))

    except Exception as ex:
        print(ex)
    
    return(text)
    


largeur_plateau = 600  # en nombre de cases
hauteur_plateau = 600  # en nombre de cases

cree_fenetre(largeur_plateau, hauteur_plateau)

recognizer = Recognizer()

while boucle:
    
    image(300,300,'assets/bg.png', ancrage = "center")
    
    mise_a_jour()
    
    ev = donne_ev()
    ty = type_ev(ev)
    
    if ty == 'Quitte':
        boucle = False
        break
        
    elif ty == 'ClicGauche':
        if 200 <= abscisse(ev) <= 400 and 200 <= ordonnee(ev) <= 400:
            text = reconnaissance()
    
    if text == "fermer" or text == "éteindre":
        boucle = False
        break
    
    if " x " in text:
        calcul(0)
        mise_a_jour()
        attend_clic_gauche()
            
    elif " + " in text:
        calcul(1)
        mise_a_jour()
        attend_clic_gauche()
        
    elif " - " in text:
        calcul(2)
        mise_a_jour()
        attend_clic_gauche()
        
    text = str()
    
    
    
ferme_fenetre()

