import PIL.Image  # Importation des library nécéssaires
from tkinter import *
import sys
from tkinter import filedialog as fd
import os, subprocess, pdb, webbrowser
import tkinter



def site():  # Fonction site
	site = Tk()
	site.title("Les infos")
	msg_site = Label(site, text="Redirection vers le site...")
	msg_site.pack(side=TOP)
	webbrowser.open(os.path.abspath('accueil.html'))

	
def menu_demare():
	menu = Tk()
	menu.title("Explications")
	message = Label(menu, bg="red",text="Cliquez sur SonaGets pour Stéganographier !\n Et sur SonaOut pour extraire l'image créee précédemment ! ")
	message.pack(side=TOP, fill=X) 
	bouton_demarer = Button(menu,fg="black", text="SonaGets", command=importimg1)
	bouton_demarer.pack(side=RIGHT) 
	bouton_stop = Button(menu,fg="black", text="SonaOut", command=importimg2)
	bouton_stop.pack(side=LEFT) 
	
def importimg1():

	filename = fd.askopenfilename()
	im1 = PIL.Image.open(filename) # Ouverture de l'Image à cacher 1
	w1, h1 = im1.size
	im1.putalpha(0)  # Insertion du canal Alpha (transparance)
	px1 = list(im1.getdata()) # Insère dans la liste le RGBA de tt les pixels.
	r1 = [] # Création des listes RGBA
	g1 = []
	b1 = []
	a1 = []
	for i in px1 :  # Affectation des valeurs aux listes respectives.
		list(i)
		r1.append(i[0])
		g1.append(i[1])
		b1.append(i[2])
		a1.append(i[3])
	print(px1[0])
	print(px1[152])
	print(px1[1052])

	rhex1 =[]  # Création des liste pour les haxadécimales
	ghex1 = []
	bhex1 = []
	ahex1 = []

	for i in r1 : # Hexadécimalage des listes.
		rhex1.append(str(bin(i)))
	for i in g1 :
		ghex1.append(str(bin(i)))
	for i in b1 :
		bhex1.append(str(bin(i)))
	for i in a1 :
		ahex1.append(str(bin(i)))
		
	print(r1[0])
	print(r1[152])
	print(r1[1052])
	
	print(rhex1[0])
	print(rhex1[152])
	print(rhex1[1052])
		
	rhex1trans = []  # Création des listes pour les hexa fort (1er)
	ghex1trans = []
	bhex1trans = []
	ahex1trans = []
	
	rhex1fort = []  # Création des listes pour les hexa fort (1er)
	ghex1fort = []
	bhex1fort = []
	ahex1fort = []
	a=0
	for i in rhex1:  # Tous les elements de rhex1
		d=rhex1[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		rhex1trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=rhex1trans[a]

		c=rhex1fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
	print(rhex1trans[0])
	print(rhex1trans[152])
	print(rhex1trans[1052])	
	
	print(rhex1fort[0])
	print(rhex1fort[152])
	print(rhex1fort[1052])
	a=0
	for i in ghex1:  # Tous les elements de rhex1
		d=ghex1[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		ghex1trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=ghex1trans[a]
		c=ghex1fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	a=0
	for i in bhex1:  # Tous les elements de rhex1
		d=bhex1[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		bhex1trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=bhex1trans[a]
		c=bhex1fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	a=0
	for i in ahex1:  # Tous les elements de rhex1
		d=ahex1[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		ahex1trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=ahex1trans[a]
		c=ahex1fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
# -------------------------------------------------------	
	filename2 = fd.askopenfilename()
	im2 = PIL.Image.open(filename2) # Ouverture de l'Image
	w2, h2 = im2.size
	im2.putalpha(0)  # Insertion du canal Alpha (transparance)
	px2 = list(im2.getdata()) # Insère dans la liste le RGBA de tt les pixels.

	r2 = [] # Création des listes RGBA
	g2 = []
	b2 = []
	a2 = []

	for i in px2 :  # Affectation des valeurs aux listes respectives.
		list(i)
		r2.append(i[0])
		g2.append(i[1])
		b2.append(i[2])
		a2.append(i[3])


	rhex2 =[]  # Création des liste pour les haxadécimales
	ghex2 = []
	bhex2 = []
	ahex2 = []

	for i in r2 : # Hexadécimalage des listes.
		rhex2.append(str(bin(i)))
	for i in g2 :
		ghex2.append(str(bin(i)))
	for i in b2 :
		bhex2.append(str(bin(i)))
	for i in a2 :
		ahex2.append(str(bin(i)))

	rhex2trans = []  # Création des listes pour les hexa fort (1er)
	ghex2trans = []
	bhex2trans = []
	ahex2trans = []
	
	rhex2fort = []  # Création des listes pour les hexa fort (1er)
	ghex2fort = []
	bhex2fort = []
	ahex2fort = []
	a=0
	for i in rhex2:  # Tous les elements de rhex1
		d=rhex2[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		rhex2trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=rhex2trans[a]

		c=rhex2fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
	a=0
	for i in ghex2:  # Tous les elements de rhex1
		d=ghex2[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		ghex2trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=ghex2trans[a]
		c=ghex2fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	a=0
	for i in bhex2:  # Tous les elements de rhex1
		d=bhex2[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		bhex2trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=bhex2trans[a]
		c=bhex2fort
		if len(b)>=4:
			c.append(b[0]+b[1]+b[2]+b[3])
		if len(b)==1 :
			c.append(b[0])
		if len(b)==2 :
			c.append(b[0]+b[1])
		if len(b)==3 :
			c.append(b[0]+b[1]+b[2])
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	a=0
	for i in ahex2:  # Tous les elements de rhex1
		d=ahex2[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		ahex2trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=ahex2trans[a]
		c=ahex2fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
	
	
# mettre le bytes fort 2 en bytes faible dans la liste.

	rhex3 = []
	ghex3 = []
	bhex3 = []
	ahex3 = []
	s=0
	for i in rhex2fort :
		rhex3.append("0b"+rhex1fort[s]+rhex2fort[s])
		s=s+1
	s=0
	for i in ghex2fort :
		bhex3.append("0b"+bhex1fort[s]+bhex2fort[s])
		s=s+1
	s=0
	for i in bhex2fort :
		ghex3.append("0b"+ghex1fort[s]+ghex2fort[s])
		s=s+1
	s=0
	for i in ahex2fort :
		ahex3.append("0b"+ahex1fort[s]+ahex2fort[s])
		s=s+1
	r3 =[]
	g3 = []
	b3 = []
	a3 = []




	for i in rhex3 :
		r3.append(int(i, base=2))
	for i in ghex3 :
		g3.append(int(i, base=2))
	for i in bhex3 :
		b3.append(int(i, base=2))
	for i in ahex3 :
		a3.append(int(i, base=2))
	
	im3 = PIL.Image.new("RGBA", (w1,h1))
	res = tuple(zip(r3, g3, b3, a3))
	x=h1
	y=w1
	c=0
	
	for a in range(0,x,1):
		for b in range(0,y,1):
			im3.putpixel((b,a), (r3[c], g3[c], b3[c], a3[c]))
			c=c+1
	im3.save("sucess.jpg")
	
		
	return 1
	
def importimg2():
	
	filename3 = fd.askopenfilename()
	im3 = PIL.Image.open(filename3)
	im3.putalpha(0) 
	w3, h3 = im3.size
	a = list(im3.getdata())
 
	
	
	
	r4 = [] # Création des listes RGBA
	g4 = []
	b4 = []
	a4 = []

	for i in a :  # Affectation des valeurs aux listes respectives.
		list(i)
		r4.append(i[0])
		g4.append(i[1])
		b4.append(i[2])
		a4.append(i[3])


	rhex4 =[]  # Création des liste pour les haxadécimales
	ghex4 = []
	bhex4 = []
	ahex4 = []

	for i in r4 : # Hexadécimalage des listes.
		rhex4.append(str(bin(i)))
	for i in g4 :
		ghex4.append(str(bin(i)))
	for i in b4 :
		bhex4.append(str(bin(i)))
	for i in a4 :
		ahex4.append(str(bin(i)))

	rhex4trans = []  # Création des listes pour les hexa fort (1er)
	ghex4trans = []
	bhex4trans = []
	ahex4trans = []
	
	rhex4fort = []  # Création des listes pour les hexa fort (1er)
	ghex4fort = []
	bhex4fort = []
	ahex4fort = []
	a=0
	for i in rhex4:  # Tous les elements de rhex1
		d=rhex4[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		rhex4trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=rhex4trans[a]

		c=rhex4fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
	a=0
	for i in ghex4:  # Tous les elements de rhex1
		d=ghex4[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		ghex4trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=ghex4trans[a]
		c=ghex4fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	a=0
	for i in bhex4:  # Tous les elements de rhex1
		d=bhex4[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		bhex4trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=bhex4trans[a]
		c=bhex4fort
		if len(b)>=4:
			c.append(b[0]+b[1]+b[2]+b[3])
		if len(b)==1 :
			c.append(b[0])
		if len(b)==2 :
			c.append(b[0]+b[1])
		if len(b)==3 :
			c.append(b[0]+b[1]+b[2])
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	a=0
	for i in ahex4:  # Tous les elements de rhex1
		d=ahex4[a].split("b") # on split le premier membre dans d pour enlever le "0b"
		ahex4trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=ahex4trans[a]
		c=ahex4fort
		if len(b)>4:
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==4 :
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3]))
		if len(b)==1 :
			c.append(str(b[0]))
		if len(b)==2 :
			c.append(str(b[0])+str(b[1]))
		if len(b)==3 :
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0:
			print("error nombre de longueur 0 !")

		a=a+1
		
	rhex4 = []
	ghex4 = []
	bhex4 = []
	ahex4 = []
	s=0
	for i in rhex4fort :
		rhex4.append("0b"+rhex4fort[s])
		s=s+1
	s=0
	for i in ghex4fort :
		bhex4.append("0b"+bhex4fort[s])
		s=s+1
	s=0
	for i in bhex4fort :
		ghex4.append("0b"+ghex4fort[s])
		s=s+1
	s=0
	for i in ahex4fort :
		ahex4.append("0b"+ahex4fort[s])
		s=s+1
	r3 =[]
	g3 = []
	b3 = []
	a3 = []

	for i in rhex4 :
		r4.append(int(i, base=2))
	for i in ghex4 :
		g4.append(int(i, base=2))
	for i in bhex4 :
		b4.append(int(i, base=2))
	for i in ahex4 :
		a4.append(int(i, base=2))
		
	im5 = PIL.Image.new("RGBA", (w3,h3))
	res = tuple(zip(r4, g4, b4, a4))
	x=h3
	y=w3
	c=0
	
	for a in range(0,x,1):
		for b in range(0,y,1):
			im5.putpixel((b,a), (r4[c], g4[c], b4[c], a4[c]))
			c=c+1
	im5.save("sucess2.jpg")
		
	
	
	return(1)
	

main = Tk()
main.title("Stegano V0.1b")


photo=PhotoImage(file="header.gif")

zone_dessin = Canvas(main,width=130,height=130,bg='yellow',bd=8,relief="ridge")

zone_dessin.create_image(75,75,image=photo)

zone_dessin.pack()



cadre = Frame(main, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)
message = Label(cadre, bg="red",text="Veuillez vous connecter pour \n acceder au programme")
message.pack(side="top", fill=X) 

bouton_quitter = Button(main,fg="red", text="Quitter", command=main.quit)
bouton_quitter.pack(side=LEFT) 

bouton_inscription = Button(main,fg="purple", text="Notre Site", command=site)
bouton_inscription.pack(side=RIGHT) 

bouton_connexion = Button(main,fg="green", text="Démarer", command=menu_demare)
bouton_connexion.pack(side=RIGHT) 


main.mainloop()



	







	
