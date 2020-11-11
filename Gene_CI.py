#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ce programme génère des conditions initiales aléatoires en fonctions des paramètres donnés.
Listes paramètres
"""


###                      Packages

import sys
import random as r

###                      Functions


###                      Main program

# Paramètres données

N_objet =  int(sys.argv[1])
m_min = int(sys.argv[2])
m_max = int(sys.argv[3])

corps = []   # liste de liste, un corps = [x, y, Vx, Vy, m]

for i in range(N_objet):
    corps += [[r.uniform(0,100),r.uniform(0,100),r.uniform(0,5),r.uniform(0,5),r.uniform(m_min, m_max)]]

# Ecriture des données dans un fichier

fichier = open('CI.dat', 'w')
for i in corps:
    fichier.write(str(i)+"\n")
fichier.close()
