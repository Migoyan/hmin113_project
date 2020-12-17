#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import sys


# Constantes
g = 1      # Constante gravitationnelle

N = int(sys.argv[1])   # Nombre de boucles temporelles 

Tmax = float(sys.argv[2])   # Temps max d'intégration

h = Tmax / N         # Pas de temps

#structure des objets [x0,y0,vx0,vy0,m]

def data_init(fileName):
    """
    Charge la liste des objets générés par le fichier Gene_CI.py ou envoyé par l'utilisateur
    Retourne une liste de type
    [[[x01], [y01], [vx01], [vy01], m1], [[x02], [y02], [vx02], [vy02], m2], ...]
    """
    corps = []
    try :
        f = open(fileName, 'r')
    except FileNotFoundError :
        print("Fichier inexistant")
        sys.exit()
    for line in f:
        tempLine = line.rstrip(', \n')
        splittedLine = tempLine.split(", ")
        corps += [[float(i) for i in splittedLine]]
    for i in corps:
        i[0] = [i[0]]
        i[1] = [i[1]]
        i[2] = [i[2]]
        i[3] = [i[3]]
    f.close()
    return corps

#calcul des accélérations
def a_x(x1,y1,x2,y2,m1,m2):
    if (x1-x2)!=0:
        return (g * m1 * m2 *
                (1. / ((x1 - x2)**2 + (y1 - y2)**2)) *
                ((x2 - x1) / m.sqrt((x1 - x2)**2 + (y1 - y2)**2)))
    else:
        return 0


def a_y(x1,y1,x2,y2,m1,m2):
    if (y1-y2)!=0:
        return (g * m1 * m2 *
                (1. / ((x1 - x2)**2 + (y1 - y2)**2)) *
                ((y2 - y1) / m.sqrt((x1 - x2)**2 + (y1 - y2)**2)))
    else:
        return 0


#méthode de runge-kutta à l'ordre 4
def k_ax(x1, y1, x2, y2, m1, m2, f):
    k = f(x1, y1, x2, y2, m1, m2)
    k2 = f(x1 + h * k/2, y1, x2, y2, m1, m2)
    k3 = f(x1 + h * k2/2, y1, x2, y2, m1, m2)
    k4 = f(x1 + h * k3, y1, x2, y2, m1, m2)
    return (k +
            2 * k2 +
            2 * k3 +
            k4) / 6

def k_ay(x1, y1, x2, y2, m1, m2, f):
    k = f(x1, y1, x2, y2, m1, m2)
    k2 = f(x1, y1+h*k/2, x2, y2, m1, m2)
    k3 = f(x1, y1+h*k2/2, x2, y2, m1, m2)
    k4 = f(x1, y1+h*k3, x2, y2, m1, m2)
    return (k +
            2 * k2 +
            2 * k3 +
            k4) / 6


#fonction pour integrer

def integration(L):
    obj = L
    t = 0
    Times = [t]
    for i in range(N):
        t += h
        Times += [t]
        #liste qui contient les accelerations au pas i
        ax = []
        ay = []
        Lobj = obj

        #calcul des accélérations un seul calcul par couple d'objet
        for obj1 in Lobj[:-1]:
            Lobj = Lobj[1:] #j'enlève l'élément de la liste pour ne pas recalculer les accélérations  associées
            
            #initialisation de la liste pour contenir les accélérations de façon temporaire
            Lax = []
            Lay = []
            #2 ième boucle pour sélectionner les objets restants 
            for obj2 in Lobj:
                Lax += [k_ax(obj1[0][i],
                             obj1[1][i],
                             obj2[0][i],
                             obj2[1][i],
                             obj1[4],
                             obj2[4],
                             a_x)] 
                Lay += [k_ay(obj1[0][i],
                             obj1[1][i],
                             obj2[0][i],
                             obj2[1][i],
                             obj1[4],
                             obj2[4],
                             a_y)]
            ax += [Lax]
            ay += [Lay]

        #ajout de l'élément i+1 pour x, y et v, initialiser à 0
        for obj1 in obj:
            for obj2 in obj1[:-1]:
                obj2 += [0]

        #calcul des vitesses
        for j in range(len(ax)):
            for k in range(len(ax[j])):
                
                #ajout des accélérations sur l'objet j
                obj[j][2][i+1] += obj[j][2][i] + h * ax[j][k] / obj[j][4]
                obj[j][3][i+1] += obj[j][3][i] + h * ay[j][k] / obj[j][4]
                
                #ajout de l'accélération sur l'objet qui luis asocier pour l'accélération
                obj[j+k+1][2][i+1] += obj[j+k+1][2][i] - h * ax[j][k] / obj[j+k+1][4]
                obj[j+k+1][3][i+1] += obj[j+k+1][3][i] - h * ay[j][k] / obj[j+k+1][4]
        
        #calcul des positions
        for objet in obj:
            objet[0][i+1] += objet[0][i] + h*objet[2][i]
            objet[1][i+1] += objet[1][i] + h*objet[3][i]
            
    return obj, Times

##                      main

Obj = data_init('CI.dat')
corps, temps = integration(Obj)


#  Enregistrement des données dans un fichiers

N_corp = 0
for corp in corps:
    N_corp += 1
    f = open("corp_" + str(N_corp), 'w')
    for i in range(len(temps)):
        f.write("{}, {}, {}, {}, {}".format(temps[i],
                                            corp[0][i],
                                            corp[1][i],
                                            corp[2][i],
                                            corp[3][i]) + "\n")
    f.close()
