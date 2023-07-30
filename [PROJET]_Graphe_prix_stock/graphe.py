import turtle
import csv

donnees = []

#Echelle d'affichage
echelle_x = 2000
echelle_y = 1000
zoom = 0.0015
N_affichage = 10

#Charement du fichier CSV
with open("[PROJET]_Graphe_prix_stock/AMZN.csv") as f:
    lecteur = csv.reader(f)
    next(lecteur,None)
    for ligne in lecteur:
        d = float(ligne[1])
        donnees.append(d)

turtle.getscreen()

#Personnalisation
turtle.title("Stock Amazon")
turtle.speed(6)
turtle.color("black", "black")

#Initialisation de la position du curseur
s = turtle.screensize()
offset_x = -s[0] + 50

#Afficher l'axe X
turtle.up()
turtle.setpos(-s[0],0)
turtle.down()
turtle.setpos(2*s[0],0)

#Afficher l'axe Y
turtle.up()
turtle.setpos(offset_x, -s[1])
turtle.down()
turtle.setpos(offset_x, 2*s[1])

turtle.color("red", "black")
offset_x = -s[0] + 50
turtle.up()
turtle.setpos(offset_x,0)
turtle.down()

#Affichage du graph
for i, v in enumerate(donnees):
    x = zoom*i*echelle_x + offset_x
    y = zoom*v*echelle_y 
    
    if i == 0:
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
    else:
        turtle.goto(x,y)

    #Afficher les valeurs sur le graph avec quelques personnalisations
    if i % N_affichage == 0:
        turtle.color("green", "black")
        turtle.write(int(v), font=("Verdana",12,"bold"))
        turtle.dot(5)
        turtle.color("red", "black")


turtle.done()