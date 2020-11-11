#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask as flk
import sys
import subprocess as sb


serveur = flk.Flask(__name__)

@serveur.route('/')  # route : localhost:5000/

def index():
    """
    Page d'acceuil du serveur flask
    """
    return "Bienvenue sur ce serveur Flask local avec lequel vous pouvez communiquer\
 pour faire des simulations du problème à n corps"

@serveur.route('/paramInit/<int:nbObj>/<int:mMin>/<int:mMax>')

def paramInit(nbObj, mMin, mMax):
    """
    Cette fonction reçoit les paramètres pour la génération de conditions initiales
    """
    bashCommand = './Gene_CI.py {} {} {}'.format(nbObj, mMin, mMax)
    process = sb.Popen(bashCommand.split(), stdout = sb.PIPE)
    output, error = process.communicate()
    if error == None:
        return "Commande executée sans problème"
    else:
        return "Erreur dans l'execution interne, \nLog d'erreur : " + str(error)
    

@serveur.route('/retourDonnees/<result>')

def retourDonnees(result):
    try:
        return flk.send_file(result)
    except FileNotFoundError:
        return "Fichier non existant"


serveur.run()
