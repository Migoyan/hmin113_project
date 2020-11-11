#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask as flk
import sys
import os


serveur = flk.Flask(__name__)

@serveur.route('/')  # route : localhost:5000/

def index():
    """
    Page d'acceuil du serveur flask
    """
    return "Bienvenue sur ce serveur Flask local avec lequel vous pouvez communiquer\
 pour faire des simulations du problème à n corps"

@serveur.route('/simulationFichier/<pathFile>')

def simulationFichier(pathFile):
    """
    Cette fonction reçoit le nom de fichier de données initiales et execute le code python de simulation dessus 
    """
    if isfile(pathFile):
        message = "Nom du fichier bien pris execution de la simulation"
    else:
        message = "Vous devez donner un nom de fichier"
    return message

@serveur.route('/retourDonnees/<result>')

def retourDonnees(result):
    return flk.send_file(result)


serveur.run()
