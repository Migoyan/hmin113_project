import tkinter as tk
import tkinter.simpledialog as tks
import tkinter.messagebox as message
from matplotlib import pyplot as plt


hauteur=700
largeur=900

def createObjet():
	n=tks.askinteger("Input","Combien d'objet voulez vous ?",parent=root)
	ob=[]
	for i in range(n):
		x=tks.askfloat("Input","X",parent=root )
		y=tks.askfloat("Input","y",parent=root )
		vx=tks.askfloat("Input","vx",parent=root )
		vy=tks.askfloat("Input","Vy",parent=root )
		ob+=[[x,y,vx,vy]]

	ask=message.askyesno("Question","voulez vous ajouter plus d'objet ?")
	if ask:
		n=tks.askinteger("Input","Combien d'objet voulez vous ?",parent=root)
		for i in range(n):
			x=tks.askfloat("Input","X",parent=root )
			y=tks.askfloat("Input","y",parent=root )
			vx=tks.askfloat("Input","vx",parent=root )
			vy=tks.askfloat("Input","Vy",parent=root )
			ob+=[[x,y,vx,vy]]
	ask=message.askyesno("Question","voulez vous lancer la simulation ?")
	if ask:
		print(ob)
	else :
		ask=message.askyesno("Question","voulez vous suprimer les objets d'objet ?")
		if ask:
			ob=[]
	print(ob)


def checkFile():
	#evoi une commande pour recuperes les fichie existent
	listFichier="" #liste des fichier contenant les differente condition initial
	print(listeFichier)
	ask=message.askyesno("Question","voulez vous afficher l'une des simulation ?")
	if ask:
		fichier=tks.askstring("Quel simulation voulez vous afficher ?")
		file=open(ficher,"r")
		data=file.readlines()
		for dat in data:
			plt.plot(dat[0],dat[1])
		plt.show()

	


"""i=tks.askfloat("Input","Vitesse",parent=root )
j=tks.askfloat("Input","Vitesse",parent=root )	
print(i,j)"""

"""strcuture bouton
bouton=Button()
bouton.pack()
"""


root=tk.Tk()
mainWindow=tk.Canvas(root,bg='White',height=hauteur,width=largeur)
mainWindow.pack(side=LEFT,padx=5,pady=5)
addresServ=tks.askstring("Input","Quelle est l'adresse du serveur ?",parent=mainWindow)
objet=tk.Button(root,text="Crée des objets",command=createObjet)
objet.pack()
check=tj.Button(root,text="Check fichier serveur",checkFile)
check.pack()
root.mainloop()