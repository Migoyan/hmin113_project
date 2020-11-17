#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ce programme génère des conditions initiales aléatoires en fonctions des paramètres donnés.
Listes paramètres
"""


###                      Packages

import sys
import random as r
import math as m

###                      Functions


###                      Main program

# Paramètres données

N_objet = int(sys.argv[1])
x_min = float(sys.argv[2])
x_max = float(sys.argv[3])
y_min = float(sys.argv[4])
y_max = float(sys.argv[5])
v_min = float(sys.argv[6])
v_max = float(sys.argv[7])
m_min = float(sys.argv[8])
m_max = float(sys.argv[9])

corps = []   # liste de liste, un corps = [x, y, Vx, Vy, m]

for i in range(N_objet):
    direction = r.uniform(0, 2*m.pi)
    direction_x = m.cos(direction)
    direction_y = m.sin(direction)
    corps += [[[r.uniform(x_min, x_max)],
               [r.uniform(y_min, y_max)],
               [r.uniform(v_min * direction_x, v_max * direction_x)],
               [r.uniform(v_min * direction_y, v_max * direction_y)],
               r.uniform(m_min, m_max)]]

# Ecriture des données dans un fichier

fichier = open('CI.dat', 'w')
for i in corps:
    fichier.write(str(i)+"\n")
fichier.close()
