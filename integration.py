from math import *
from matplotlib import pyplot as plt


g=0.001
h=1./100


Obj=[]


#structure des objets [x0,y0,vx0,vy0,m]

Obj+=[[1,0,0,0,10]]
Obj+=[[0,0,0,0,100]]
Obj+=[[0,1,0,0,90]]

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



def integration(L):
	obj=init_obj(L)
	for i in range(10):
		ax=[]
		ay=[]
		Lobj=obj
		for obj1 in Lobj[:-1]:
			Lobj=Lobj[1:]
			Lax=[]
			Lay=[]
			for obj2 in Lobj:
				Lax+=[a_x(obj1[0][i],obj1[1][i],obj2[0][i],obj2[1][i],obj1[4],obj2[4])]
				Lay+=[a_y(obj1[0][i],obj1[1][i],obj2[0][i],obj2[1][i],obj1[4],obj2[4])]
			ax+=[Lax]
			ay+=[Lay]
		for obj1 in obj:
			for obj2 in obj1[:-1]:
				obj2+=[0]
		for j in range(len(ax)):
			for k in range(len(ax[j])):
				obj[j][2][i+1]+=obj[j][2][i]+h*ax[j][k]/obj[j][4]
				obj[j][3][i+1]+=obj[j][3][i]+h*ay[j][k]/obj[j][4]
				obj[j+k+1][2][i+1]+=obj[j+k+1][2][i]-h*ax[j][k]/obj[j+k+1][4]
				obj[j+k+1][3][i+1]+=obj[j+k+1][3][i]-h*ay[j][k]/obj[j+k+1][4]
		for objet in obj:
			objet[0][i+1]+=objet[0][i]+h*objet[2][i]
			objet[1][i+1]+=objet[1][i]+h*objet[3][i]
			print(objet[0])
	#print(obj[0])
	return(obj)





lis=integration(Obj)
fig=plt.figure()
plt.plot(lis[0][0],lis[0][1])
plt.show()