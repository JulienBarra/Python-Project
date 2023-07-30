import random
options = ["pierre", "papier", "ciseaux"]

points_joueur = 0
points_ordinateur = 0
continuer = True

while (continuer):
    joueur = input("pierre, papier, ciseaux ? ou tapez Fin pour stopper le jeu !")
    ordinateur = random.choice(options)

    if (joueur == "Fin"):
        continuer = False
    elif (joueur == ordinateur):
        print ("égalité !")

    elif (joueur == "pierre"):
        if (ordinateur == "papier"):
            print ("Perdu ! L'ordinateur a joué papier !")
            points_ordinateur = points_ordinateur + 1
        else:
            print ("Gagné ! L'ordinateur a joué ciseaux !")
            points_joueur = points_joueur + 1

    elif (joueur == "ciseaux"):
        if (ordinateur == "pierre"):
            print("Perdu ! L'ordinateur a joué pierre !")
            points_ordinateur = points_ordinateur + 1
        else:
            print("Gagné ! L'ordinateur a joué papier !")
            points_joueur = points_joueur + 1

    elif (joueur == "papier"):
        if (ordinateur == "ciseaux"):
            print("Perdu ! L'ordinateur a joué ciseaux !")
            points_ordinateur = points_ordinateur + 1
        else:
            print("Gagné ! L'ordinateur a joué pierre !")
            points_joueur = points_joueur + 1

    else:
        print ("Votre choix n'est pas correct, veuillez vérifier l'orthographe !")
        ordinateur = random.choice(options)
        print("-----Tour suivant-----")

print ("-----Points-----")
print(f"Points du joueur : {points_joueur}")
print(f"Points de l'ordinateur : {points_ordinateur}")