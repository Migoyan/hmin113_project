#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ce programme génère des conditions initiales aléatoires en fonctions des paramètres donnés.
Listes paramètres
"""


###                      Packages

import sys

###                      Functions


###                      Main program

# Vérification de la bonne valeur du paramètre donné, N_objet étant le nombre d'objet
try :
    N_objet =  int(sys.argv[1])  #ValueError
    if N_objet < 0 :
        raise ValueError
    else :
        print("Paramètre correct, valeur : ", N_objet, "\n" +
              "Execution du code")
except ValueError:
    print("Il faut un nombre entier positif, relancer le programme")



# Ecriture des données dans un fichier
