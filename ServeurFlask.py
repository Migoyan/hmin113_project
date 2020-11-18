#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask as flk
import sys
import subprocess as sb

UPLOAD_FOLDER = '/'

serveur = flk.Flask(__name__)
serveur.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@serveur.route('/')  # route : localhost:5000/

def index():
    """
    Page d'acceuil du serveur flask
    """
    return "Bienvenue sur ce serveur Flask local avec lequel vous pouvez communiquer\
 pour faire des simulations du problème à n corps"

@serveur.route('/paramInit/<int:nbObj>/<float:xMin>/<float:xMax>/<float:yMin>/<float:yMax>/<float:vMin>/<float:vMax>/<float:mMin>/<float:mMax>')

def param_init(nbObj, xMin, xMax, yMin, yMax, vMin, vMax, mMin, mMax):
    """
    Cette fonction reçoit les paramètres pour la génération de conditions initiales aléatoires
    """
    bashCommand = './Gene_CI.py {} {} {} {} {} {} {} {} {}'.format(nbObj,
                                                                   xMin, xMax, yMin, yMax,
                                                                   vMin, vMax,
                                                                   mMin, mMax)
    process = sb.Popen(bashCommand.split(), stdout = sb.PIPE)
    output, error = process.communicate()
    if error == None:
        return "Commande executée sans problème"
    else:
        return "Erreur dans l'execution interne, \nLog d'erreur : " + str(error)

@serveur.route('/uploadCIFile', methods = ['POST'])

def upload_CI_file():
    """
    Cette fonction permet de recevoir un fichier de l'utilisateur
    Pour uploadé un fichier (commande bash) :
    curl -X POST -F filename=@Nom_fichier http://localhost:5000/uploadCIFile
    """
    f = flk.request.files['filename']
    f.save("CI.dat")
    return "fichier uploadé"

@serveur.route('/retourDonnees/<result>')

def retour_donnees(result):
    try:
        return flk.send_file(result)
    except FileNotFoundError:
        return "Fichier non existant"


serveur.run()
