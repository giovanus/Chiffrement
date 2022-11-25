# -*- coding: utf-8 -*-
from functions import * 
x=int(input('Entrez 0 pour saisir un texte a crypter ou \n Entrez 1 pour charger un fichier txt : '))
while x!=0 and x!=1  :
    x=int(input('Entrez 0 pour saisir un texte a crypter ou \n Entrez 1 pour charger un fichier txt : '))
if x==0 :
    message=input('Entrez le message a crypter : ')
    key=input('Entrez la clée : ')
    while not keyChecker(key):
        key=input('la clé ne doit contenir que des lettres de l\'alphabet : ')
    print('le message crypté est \n '+crypter(message, key))
else :
    Dir=input('Entrez le chemin d\'accès du fichier : ')
    key=input('Entrez la clée : ')
    result=cryptFromFile(Dir,'FEU')
    print(result)

