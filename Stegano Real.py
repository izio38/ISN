import PIL.Image  # Importation des library nécéssaires
from tkinter import *
import sys
from tkinter import filedialog as fd
import os, subprocess, pdb, webbrowser
import tkinter



def site():  # Fonction site
	site = Tk()  #Ouverture nouvelle fenetre
	site.title("Les infos")
	msg_site = Label(site, text="Redirection vers le site...")
	msg_site.pack(side=TOP)
	webbrowser.open(os.path.abspath('site/accueil.html')) #Ouverture du site static en html

	
def menu_demare(): #Fonction demarrer
	menu = Tk() #Ouverture nouvelle fenetre
	menu.title("Explications")
	message = Label(menu, bg="red",text="Cliquez sur SonaGets pour Stéganographier !\n Et sur SonaOut pour extraire l'image créee précédemment ! ")
	message.pack(side=TOP, fill=X) 
	bouton_demarer = Button(menu,fg="black", text="SonaGets", command=importimg1) # appel fonction importimg1
	bouton_demarer.pack(side=RIGHT) 
	bouton_stop = Button(menu,fg="black", text="SonaOut", command=importimg2) # appel fonction importimg2
	bouton_stop.pack(side=LEFT) 
	
def importimg1(): #Fonction importimg1

	filename = fd.askopenfilename() #Demande de séléctionner un fichier à l'utilisateur
	im1 = PIL.Image.open(filename) # Ouverture de l'Image à cacher 1 qui à été séléctionné
	w1, h1 = im1.size #dans w1 on met le nombre de px en largeur et dans h1 le nombre de px en hauteur
	im1.putalpha(0)  # Insertion du canal Alpha (transparance)
	px1 = list(im1.getdata()) # Insère dans la liste px1 le RGBA de tous les pixels.
	r1 = [] # Création des listes RGBA
	g1 = []
	b1 = []
	a1 = []
	for i in px1 :  # Affectation des valeurs aux listes respectives.
		list(i)
		r1.append(i[0]) #valeur en rouge (255, 0, 25, etc...)
		g1.append(i[1]) #idem pour vert
		b1.append(i[2]) # bleu
		a1.append(i[3]) # canal alpha


	rhex1 =[]  # Création des liste pour les haxadécimales
	ghex1 = []
	bhex1 = []
	ahex1 = []

	for i in r1 : # mise en binaire de toutes les valeurs des listes précédentes.
		rhex1.append(str(bin(i))) # 255 ->> 0b11111111
	for i in g1 : # idem pour les verts
		ghex1.append(str(bin(i)))
	for i in b1 : #bleu
		bhex1.append(str(bin(i)))
	for i in a1 : #canal alpha
		ahex1.append(str(bin(i)))
		
	rhex1trans = []  # Création des listes de transitions entre rhex1 vers rhex1fort
	ghex1trans = []
	bhex1trans = []
	ahex1trans = []
	
	rhex1fort = []  # Création des listes pour les premiers binaires représentatifs
	ghex1fort = []
	bhex1fort = []
	ahex1fort = []
	a=0
	for i in rhex1:  # Tous les elements de rhex1
		d=rhex1[a].split("b") # on split le premier membre dans d pour enlever le "0b" et pouvoir traiter les binaires en int
		rhex1trans.append(d[1]) # dans la liste de transition on ajoute la partie non "0b"
		b=rhex1trans[a]
		c=rhex1fort
		if len(b)>=4: # Si la longueur du nombre est supérieur à 4
			c.append(str(b[0])+str(b[1])+str(b[2])+str(b[3])) # Alors il peut avoir comme binaire premier 4 chiffres.
		if len(b)==1 : # Le cas où la longueur est =1
			c.append(str(b[0])) #Alors le bit fort est unique.
		if len(b)==2 : # Cas où la longueur est =2
			c.append(str(b[0])+str(b[1])) #Il peut contenir 2 chiffre
		if len(b)==3 : #Idem avec 3
			c.append(str(b[0])+str(b[1])+str(b[2]))
		if len(b)==0: # Test erreur car bug...
			print("error nombre de longueur 0 !")

		a=a+1 #Incrémentation de a
	a=0
	for i in ghex1:  # On répète l'opération avec la liste des valeurs de pixels verts.
		d=ghex1[a].split("b") 
		ghex1trans.append(d[1]) 
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
	for i in bhex1:   # On répète l'opération avec la liste des valeurs de pixels bleu.
		d=bhex1[a].split("b") 
		bhex1trans.append(d[1]) 
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
	for i in ahex1:   # On répète l'opération avec la liste des valeurs des pixels du canal alpha.
		d=ahex1[a].split("b") 
		ahex1trans.append(d[1]) 
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
# ----------------Nous allons répéter la même opération avec l'image numéro 2	
	filename2 = fd.askopenfilename()
	im2 = PIL.Image.open(filename2) # Ouverture de l'Image
	w2, h2 = im2.size
	im2.putalpha(0)  
	px2 = list(im2.getdata()) 

	r2 = [] 
	g2 = []
	b2 = []
	a2 = []

	for i in px2 :  
		list(i)
		r2.append(i[0])
		g2.append(i[1])
		b2.append(i[2])
		a2.append(i[3])
# px2 --> r2 

	rhex2 =[]  
	ghex2 = []
	bhex2 = []
	ahex2 = []

	for i in r2 : 
		rhex2.append(str(bin(i)))
	for i in g2 :
		ghex2.append(str(bin(i)))
	for i in b2 :
		bhex2.append(str(bin(i)))
	for i in a2 :
		ahex2.append(str(bin(i)))
		
# r2 --> rhex2

	rhex2trans = [] 
	ghex2trans = []
	bhex2trans = []
	ahex2trans = []
	
	rhex2fort = [] 
	ghex2fort = []
	bhex2fort = []
	ahex2fort = []
	a=0
	for i in rhex2:  
		d=rhex2[a].split("b") 
		rhex2trans.append(d[1])
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
# rhex2 --> rhex2fort : Nous avons les bits forts de l'image 2 pour les rouges, faisons pareil avec les autres.
	a=0
	for i in ghex2:  # Bit fort : VERT
		d=ghex2[a].split("b") 
		ghex2trans.append(d[1]) 
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
	for i in bhex2: #Bit fort : BLEU
		d=bhex2[a].split("b") 
		bhex2trans.append(d[1]) 
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
	for i in ahex2:  # Bit fort : ALPHA
		d=ahex2[a].split("b") 
		ahex2trans.append(d[1]) 
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
	
	
# L'Etape qui suit consiste à mettre les bits forts de l'image 1 en tant que bits forts dans l'image 3 mais nous devons aussi
# Mettre les bits forts de l'image dans en tant que bits faibles dans l'image 3

	rhex3 = [] #Création des listes
	ghex3 = []
	bhex3 = []
	ahex3 = []
	s=0
	for i in rhex2fort : # Pour tous i dans la liste rhex2fort :
		rhex3.append("0b"+rhex1fort[s]+rhex2fort[s]) # On place "0b" avant les bits pour "reconstituer" le bit entièrement puis on y ajoute les bits forts de l'im1 et les bits fort de l'im2
		s=s+1
	s=0
	for i in ghex2fort :  # On fait la même chose avec les Verts
		bhex3.append("0b"+bhex1fort[s]+bhex2fort[s])
		s=s+1
	s=0
	for i in bhex2fort : # Avec les bleus
		ghex3.append("0b"+ghex1fort[s]+ghex2fort[s])
		s=s+1
	s=0
	for i in ahex2fort : # Avec le canal alpha
		ahex3.append("0b"+ahex1fort[s]+ahex2fort[s])
		s=s+1
		
	r3 =[] #Création des listes finales de valeur "normale" (255,26,53)
	g3 = []
	b3 = []
	a3 = []




	for i in rhex3 : 
		r3.append(int(i, base=2)) # On place dans les listes finales les nombres/chiffres.
	for i in ghex3 :
		g3.append(int(i, base=2)) # Idem pour vert
	for i in bhex3 :
		b3.append(int(i, base=2)) #bleu
	for i in ahex3 :
		a3.append(int(i, base=2)) #canal alpha
	
	im3 = PIL.Image.new("RGBA", (w1,h1)) #Création d'une image3 de mode RGBA et de taille w1,h1 (idem que im1)
	res = tuple(zip(r3, g3, b3, a3)) # Ligne innutil car non maîtrise mais cela est "apparement" efficace quand on sait l'utiliser.
	x=h1
	y=w1
	c=0
	for a in range(0,x,1): # Pour chaque colonne
		for b in range(0,y,1): #pour chaque ligne
			im3.putpixel((b,a), (r3[c], g3[c], b3[c], a3[c])) #Mettre dans le pixel visé, les valeurs des listes précedentes.
			c=c+1 #incrémentation de c
	im3.save("sucess.jpg") # On enregistre l'image finale
	
		
	return 1 #Tout c'est bien passé ! return 1
	
def importimg2(): # C'est la fonction "inverse"
	
	filename3 = fd.askopenfilename() # on demande de selectionner l'image stéganographié
	im3 = PIL.Image.open(filename3) # on l'ouvre et on la place dans im3
	im3.putalpha(0) # en n'oubliant pas le canal alpha
	w3, h3 = im3.size # de taille connue w3, h3
	a = list(im3.getdata()) # on récupère les valeurs de chaque pixel de l'im3 dans une liste "a"
 
	
	#################  LES LIGNES SUIVANTES SONT IDENTIQUES AU MECANISME PRECEDENT (jusqu'à ligne : 496) ########
	
	r4 = [] 
	g4 = []
	b4 = []
	a4 = []

	for i in a :  
		list(i)
		r4.append(i[0])
		g4.append(i[1])
		b4.append(i[2])
		a4.append(i[3])


	rhex4 =[]  
	ghex4 = []
	bhex4 = []
	ahex4 = []

	for i in r4 :
		rhex4.append(str(bin(i)))
	for i in g4 :
		ghex4.append(str(bin(i)))
	for i in b4 :
		bhex4.append(str(bin(i)))
	for i in a4 :
		ahex4.append(str(bin(i)))

	rhex4trans = [] 
	ghex4trans = []
	bhex4trans = []
	ahex4trans = []
	
	rhex4fort = [] 
	ghex4fort = []
	bhex4fort = []
	ahex4fort = []
	a=0
	for i in rhex4:
		d=rhex4[a].split("b") 
		rhex4trans.append(d[1]) 
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
	for i in ghex4:  
		d=ghex4[a].split("b")
		ghex4trans.append(d[1]) 
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
	for i in bhex4:  
		d=bhex4[a].split("b") 
		bhex4trans.append(d[1]) 
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
	for i in ahex4: 
		d=ahex4[a].split("b") 
		ahex4trans.append(d[1]) 
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
##############################################################################

	im4 = PIL.Image.new("RGBA", (w3,h3)) #on créer l'image 4
	res = tuple(zip(r4, g4, b4, a4)) # toujours cette ligne innutile
	x=h3 
	y=w3
	c=0 # initialisation de c
	
	for a in range(0,x,1): 
		for b in range(0,y,1):
			im4.putpixel((b,a), (r4[c], g4[c], b4[c], a4[c]))
			c=c+1
	im4.save("sucess2.jpg") # on sauvegarde l'image dans sucess2.jpg
		
	
	
	return(1)
	

main = Tk() # Fenetre principale de Sonagets
main.title("Sonagets V0.1b") # On y met un titre


photo=PhotoImage(file="header.gif") # Une image

zone_dessin = Canvas(main,width=130,height=130,bg='yellow',bd=8,relief="ridge")

zone_dessin.create_image(75,75,image=photo)

zone_dessin.pack() # pack de la zone et donc de l'image



cadre = Frame(main, width=768, height=576, borderwidth=1) #Création d'un cadre
cadre.pack(fill=BOTH)
message = Label(cadre, bg="red",text="Veuillez cliquer sur \n Démarrer pour débuter l'expérience !")
message.pack(side="top", fill=X) 

bouton_quitter = Button(main,fg="red", text="Quitter", command=main.quit) # Ajout du bouton quitter
bouton_quitter.pack(side=LEFT) 

bouton_inscription = Button(main,fg="purple", text="Notre Site", command=site) # Ajout du bouton notre site
bouton_inscription.pack(side=RIGHT) 

bouton_connexion = Button(main,fg="green", text="Démarrer", command=menu_demare) # ajout du bouton démarrer
bouton_connexion.pack(side=RIGHT) 


main.mainloop() # Mainloop()



	







	
