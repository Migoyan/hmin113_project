#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.simpledialog as tks
import tkinter.messagebox as message
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess as sb
import time 
import os


hauteur=20
largeur=20
fich_select=""
numsimu=len(os.listdir("initial_data"))

def createObjet():
    global fich_select,numsimu
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
        numsimu+=1
        nomfich="initial_data/"+"CI"+str(numsimu)+".dat"
        fich=open(nomfich,"w")
        for o in ob:
            for char in o:
                fich.write(str(char)+", ")
            fich.write("\n")
        fich.close()    
    fich_select=nomfich
    #print(ob)

def lanceSimul():
    global fich_select
    ask=message.askyesno("Question","voulez vous lancer la simulation?"+fich_select)
    fich=open(fich_select,"r")
    dat=fich.readlines()
    num_simu=float(fich_select[-5])
    n=len(dat)
    if ask:
        curlcommande="curl -X POST -F filename="+fich_select+" "+adrresServ+"/uploadCIFile"
        process = sb.Popen(curlcommande.split(), stdout = sb.PIPE)
        output,error = process.communicate()
        time.sleep(3) #temps de pausse pour laisser le temps au serve de faire les calcules
        for i in range(n):
            corp="corp_"+str(1+i)
            curlcommande="curl "+adrresServ+"/retourDonnees/"+corp+"> plotdata/"+str(num_simu)+"/"+corp
            process = sb.Popen(curlcommande.split(), stdout = sb.PIPE)
            output,error = process.communicate()
        ask=message.askyesno("Question","voulez vous ploter les donné?")
        if ask:
            plotSimu(num_simu)

def checkFile(numsimu):
    global fich_select
    init_data=os.listdir("initial_data")
    for i in init_data:
        data=open("initial_data/"+i,"r")
        print(i,data.readlines())
    ask=message.askyesno("Question","Voulez vous selectionner un fichier ?")
    if ask:
        fich_select=tks.askstring("Input","Entrer le nom du fichier")
        fich_select="initial_data/"+fich_select
        ask=message.askyesno("Question","Voulez vous lancer la simulation ?")
        num_simu=float(fich_select[-5])
        if ask :
            lanceSimul(num_simu)


def plotSimu(num_simu=0):
    if num_simu == 0 :
        num_simu=tks.askinteger("Input","Quelle simulation voulez-vous afficher ?",parent=root)
    corps=os.listdir("plotdata/"+str(num_simu))
    for fich in corps:
        coord=data.readlines()
        corp = []
        try :
            data=open("plotdata/"+str(num_simu)+"/"+fich,"r")
        except FileNotFoundError :
            print("Fichier inexistant")
        for line in data:
            tempLine = line.rstrip('\n')
            splittedLine = tempLine.split(", ")
            corp += [[float(i) for i in splittedLine]]
            corp_array = np.array(corp)
        data.close()
        plt.plot(corp_array[:, 1], corp_array[:, 2])
    plt.show()


def random_simu():
        global numsimu
        n=tks.askinteger("Input","Combien d'objet voulez vous ?",parent=root)
        x=tks.askfloat("Input","X_min",parent=root )
        x_max=tks.askfloat("Input","X_max",parent=root )
        y=tks.askfloat("Input","Y_min",parent=root )
        y_max=tks.askfloat("Input","Y_max",parent=root )
        v=tks.askfloat("Input","v_min",parent=root )
        v_max=tks.askfloat("Input","v_max",parent=root )
        M_min=tks.askfloat("Input","M_min",parent=root )
        M_max=tks.askfloat("Input","M_max",parent=root )
        ask=message.askyesno("Question","Voulez vous lancer la simulation ?")
        if ask:
            curlcommande=("curl "+addresServ+"/paramInit/"+
                          str(n)+"/"+
                          str(x)+"/"+
                          str(x_max)+"/"+
                          str(y)+"/"+
                          str(y_max)+"/"+
                          str(v)+"/"+
                          str(v_max)+"/"+
                          str(M_min)+"/"+
                          str(M_max))
            process = sb.Popen(curlcommande.split(), stdout = sb.PIPE)
            output,error = process.communicate()
            numsimu+=1
            curlcommande="curl "+addresServ+"/retourDonnees/CI.dat > initial_data/CI"+str(numsimu)+".dat"
            process = sb.Popen(curlcommande.split(), stdout = sb.PIPE)
            output,error = process.communicate()


"""i=tks.askfloat("Input","Vitesse",parent=root )
j=tks.askfloat("Input","Vitesse",parent=root )  
print(i,j)"""

"""strcuture bouton
bouton=Button()
bouton.pack()
"""

    
root=tk.Tk()
mainWindow=tk.Canvas(root,bg='White',height=hauteur,width=largeur)
mainWindow.pack(side="left",padx=5,pady=5)

addresServ=tks.askstring("Input","Quelle est l'adresse du serveur ?",parent=mainWindow)

objet=tk.Button(root,text="Crée des objets",command=createObjet)
objet.pack()

check=tk.Button(root,text="Check fichier ",command=lambda :checkFile(numsimu))
check.pack()

upload=tk.Button(root,text="lancer la simulation ",command=lanceSimul)
upload.pack()

random_simu=tk.Button(root,text="random simulation ",command=random_simu)
random_simu.pack()

plote=tk.Button(root,text="plot",command=plotSimu)
plote.pack()

root.mainloop()
num_fich.close()
