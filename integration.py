#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt


# Constantes
g=1      # Constante gravitationnelle

h=0.00001         # Pas de temps


Obj=[]


#structure des objets [x0,y0,vx0,vy0,m]

Obj+=[[[1000],[0],[0],[10],1]]
Obj+=[[[0],[0],[0],[0],10000]]

#calcul des accélérations
def a_x(x1,y1,x2,y2,m1,m2):
	if (x1-x2)!=0:
		return g*m1*m2*(1./((x1-x2)**2+(y1-y2)**2))*((x2-x1)/m.sqrt((x1-x2)**2+(y1-y2)**2))
	else:
		return 0


def a_y(x1,y1,x2,y2,m1,m2):
	if (y1-y2)!=0:
		return g*m1*m2*(1./((x1-x2)**2+(y1-y2)**2))*((y2-y1)/m.sqrt((x1-x2)**2+(y1-y2)**2))
	else:
		return 0


#méthode de runge-kutta à l'ordre 4
def k_ax(x1,y1,x2,y2,m1,m2,f):
	k=f(x1,y1,x2,y2,m1,m2)
	k2=f(x1+h*k/2,y1,x2,y2,m1,m2)
	k3=f(x1+h*k2/2,y1,x2,y2,m1,m2)
	k4=f(x1+h*k3,y1,x2,y2,m1,m2)
	return (k+2*k2+2*k3+k4)/6

def k_ay(x1,y1,x2,y2,m1,m2,f):
	k=f(x1,y1,x2,y2,m1,m2)
	k2=f(x1,y1+h*k/2,x2,y2,m1,m2)
	k3=f(x1,y1+h*k2/2,x2,y2,m1,m2)
	k4=f(x1,y1+h*k3,x2,y2,m1,m2)
	return(k+2*k2+2*k3+k4)/6


#fonction pour integré

def integration(L):
	obj=L
	for i in range(100000):
		#liste qui contient les accelerations au pas i
		ax=[]
		ay=[]
		Lobj=obj

		#calcul des accelerations un seul calcul par couple d'objet
		for obj1 in Lobj[:-1]:
			Lobj=Lobj[1:] #j'enlève l'élément de la liste pour ne pas recalculer les accélerations  associées
			
			#initialisation de liste pour contenir les accélérations de façon temporaire
			Lax=[]
			Lay=[]
			#2 ième boucle pour sélectionner les objets restants 
			for obj2 in Lobj:
				Lax+=[k_ax(obj1[0][i],obj1[1][i],obj2[0][i],obj2[1][i],obj1[4],obj2[4],a_x)] 
				Lay+=[k_ay(obj1[0][i],obj1[1][i],obj2[0][i],obj2[1][i],obj1[4],obj2[4],a_y)]
			ax+=[Lax]
			ay+=[Lay]

		#ajout de l'élément i+1 pour x, y et v, initialiser à 0
		for obj1 in obj:
			for obj2 in obj1[:-1]:
				obj2+=[0]

		#calcul des vitesses
		for j in range(len(ax)):
			for k in range(len(ax[j])):
				#ajout des accélérations sur l'objet j
				obj[j][2][i+1]+=obj[j][2][i]+h*ax[j][k]/obj[j][4]
				obj[j][3][i+1]+=obj[j][3][i]+h*ay[j][k]/obj[j][4]
				#ajout de l'accélération sur l'objet qui luis asocier pour l'accélération
				obj[j+k+1][2][i+1]+=obj[j+k+1][2][i]-h*ax[j][k]/obj[j+k+1][4]
				obj[j+k+1][3][i+1]+=obj[j+k+1][3][i]-h*ay[j][k]/obj[j+k+1][4]
		
		#calcul des positions
		for objet in obj:
			objet[0][i+1]+=objet[0][i]+h*objet[2][i]
			objet[1][i+1]+=objet[1][i]+h*objet[3][i]
			#print(objet[0])
	#print(obj[0])
	return(obj)





lis=integration(Obj)
fig=plt.figure()
plt.plot(lis[0][0],lis[0][1])
plt.show()
