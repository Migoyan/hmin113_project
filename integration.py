#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import *
from matplotlib import pyplot as plt


g=0.00001

h=0.00001


Obj=[]


#structure des objets [x0,y0,vx0,vy0,m]

Obj+=[[1,0,0,0,1]]
Obj+=[[0,0,0,0,100000]]

#calcule des acceleration
def a_x(x1,y1,x2,y2,m1,m2):
	if (x1-x2)!=0:
		return -g*m1*m2*(1./((x1-x2)**2+(y1-y2)**2))*((x1-x2)/sqrt((x1-x2)**2+(y1-y2)**2))
	else:
		return 0


def a_y(x1,y1,x2,y2,m1,m2):
	if (y1-y2)!=0:
		return -g*m1*m2*(1./((x1-x2)**2+(y1-y2)**2))*((y1-y2)/sqrt((x1-x2)**2+(y1-y2)**2))
	else:
		return 0


#remplace les valeur de x,y et v par des list
def init_obj(L):
	for i in range(len(L)):
		x=L[i][0]
		y=L[i][1]
		vx=L[i][2]
		vy=L[i][3]
		L[i][0]=[x]
		L[i][1]=[y]
		L[i][2]=[vx]
		L[i][3]=[vx]
	return(L)


#methode de runge-kutta à l'ordre 4
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


#fonction pour integre 

def integration(L):
	obj=init_obj(L)
	for i in range(100000):
		#liste qui contiene les acceleration au pas i
		ax=[]
		ay=[]
		Lobj=obj

		#calcule des accelerations un seul calcule par couple d'objet
		for obj1 in Lobj[:-1]:
			Lobj=Lobj[1:] #j'enleve l'élement de la liste pour ne pas recalculer les accéleration  associer
			
			#initialisation de liste pour contenir les accéleration de façon temporaire
			Lax=[]
			Lay=[]
			#2 eme boucle pour selectionner les objet restant 
			for obj2 in Lobj:
				Lax+=[k_ax(obj1[0][i],obj1[1][i],obj2[0][i],obj2[1][i],obj1[4],obj2[4],a_x)] 
				Lay+=[k_ay(obj1[0][i],obj1[1][i],obj2[0][i],obj2[1][i],obj1[4],obj2[4],a_y)]
			ax+=[Lax]
			ay+=[Lay]

		#ajout de l'element i+1 pour x,y et v , initialiser à 0
		for obj1 in obj:
			for obj2 in obj1[:-1]:
				obj2+=[0]

		#calcule des vitesse
		for j in range(len(ax)):
			for k in range(len(ax[j])):
				#ajout des acceleration sur l'objet j
				obj[j][2][i+1]+=obj[j][2][i]+h*ax[j][k]/obj[j][4]
				obj[j][3][i+1]+=obj[j][3][i]+h*ay[j][k]/obj[j][4]
				#ajout de l'acceleration sur l'objet qui luis asocier pour l'accelaration
				obj[j+k+1][2][i+1]+=obj[j+k+1][2][i]-h*ax[j][k]/obj[j+k+1][4]
				obj[j+k+1][3][i+1]+=obj[j+k+1][3][i]-h*ay[j][k]/obj[j+k+1][4]
		
		#calcule des position
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