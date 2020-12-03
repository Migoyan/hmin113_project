#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.simpledialog as tks
import tkinter.messagebox as message
from matplotlib import pyplot as plt
import sys
import subprocess as sb

hauteur=700
largeur=900
fich_select=""

def createObjet():
    n=tks.askinteger("Input","Combien d'objet voulez vous ?",parent=root)
    ob=[]
    for i in range(n):
        x=tks.askfloat("Input","X",parent=root )
        y=tks.askfloat("Input","y",parent=root )
        vx=tks.askfloat("Input","vx",parent=root )
        vy=tks.askfloat("Input","Vy",parent=root )
        m=tks.askfloat("Input","m",parent=root )
        ob+=[[x,y,vx,vy,m]]

    ask=message.askyesno("Question","voulez vous ajouter plus d'objet ?")
    if ask:
        n=tks.askinteger("Input","Combien d'objet voulez vous ?",parent=root)
        for i in range(n):
            x=tks.askfloat("Input","X",parent=root )
            y=tks.askfloat("Input","y",parent=root )
            vx=tks.askfloat("Input","vx",parent=root )
            vy=tks.askfloat("Input","Vy",parent=root )
            m=tks.askfloat("Input","m",parent=root)
            ob+=[[x,y,vx,vy,m]]

    ask=message.askyesno("Question","voulez vous suprimer les objets d'objet ?")
    if ask:
        ob=[]
    else :
        nbfichier=1
        nomfich="initial_data/"+"CI"+str(nbfichier)+".dat"
        fich=open(nomfich,"w")
        for o in ob:
            for char in o:
                fich.write(str(char)+", ")
            fich.write("\n")
        fich.close()    
    fich_select=nomfich
    #print(ob)

def lanceSimul():
    ask=message.askyesno("Question","voulez vous lancer la simulation?")
    if ask:
        """curlcommande="curl -X POST -F filename="+fich_select+" "+adrresServ+/uploadCIFile"
        process = sb.Popen(curlcommande.split(), stdout = sb.PIPE)
        output,error = process.communicate()"""
        """curlcommande=adrresServ+"/retourDonnees/<result>"
        process = sb.Popen(curlcommande.split(), stdout = sb.PIPE)
        output,error = process.communicate()"""
    ask=message.askyesno("Question","voulez vous ploter les donné?")
    if ask:
        plotSimu()

def checkFile():
    """lscommande="ls initial_data"
    process = sb.Popen(lscommande.split(), stdout = sb.PIPE)
    output,error = process.communicate()"""
    output=[]
    for fich in output:
        data=open("initial_data/"+fich,"r")
        print(fish,data)
    ask=message.askyesno("Question","Voulez vous selectionner un fichier ?")
    if ask:
        fich_select=tks.askstring("Input","Entrer le nom du fichier")
        ask=message.askyesno("Question","Voulez vous lancer la simulation ?")
        if ask :
            lanceSimul()

def plotSimu():
    """lscommande="ls plotdata/"+str(numsimiu)
    process = sb.Popen(lscommande.split(), stdout = sb.PIPE)
    output,error = process.communicate()"""
    for fich in output:
        data=open("plotdata/"+str(numsimiu)+fich,"r")
        coord=data.readlines()
        plt.plot(coord[1],coord[2])
    plt.show()



"""i=tks.askfloat("Input","Vitesse",parent=root )
j=tks.askfloat("Input","Vitesse",parent=root )  
print(i,j)"""

"""strcuture bouton
bouton=Button()
bouton.pack()
"""
"""try:
    lscommande="ls initial_data"
    process = sb.Popen(lscommande.split(), stdout = sb.PIPE)
    output,error = process.communicate()

    print(output)
except:
    mkdircommande="mkdir initial_data"
    process=sb.Popen(mkdircommande.split(), stdout = sb.PIPE)
    output,error=process.communicate()"""

root=tk.Tk()
mainWindow=tk.Canvas(root,bg='White',height=hauteur,width=largeur)
mainWindow.pack(side="left",padx=5,pady=5)

addresServ=tks.askstring("Input","Quelle est l'adresse du serveur ?",parent=mainWindow)

objet=tk.Button(root,text="Crée des objets",command=createObjet)
objet.pack()

check=tk.Button(root,text="Check fichier ",command=checkFile)
check.pack()

upload=tk.Button(root,text="lancer la simulation ",command=lanceSimul)
upload.pack()

plote=tk.Button(root,text="plot",command=plotSimu)
plote.pack()

root.mainloop()