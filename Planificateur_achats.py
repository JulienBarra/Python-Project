class Achats:
    def __init__(self):
        self.produits = {}
    def ajouter (self, achat, prix): 
        self.produits[achat] = prix
    def supprimer (self, achat):
        if achat in self.produits:
            del self.produits[achat]
        else:
            print("Erreur : Ce produit ne fait pas partie de cette liste")
    def prix_total(self):
        total = 0
        for a in self.produits:
            total += self.produits[a]
        print(f"Prix total = {total}")
    def afficher (self):
        print("-------------------")
        for i, a in enumerate(self.produits):
            print(f"{i} : {a} - {self.produits[a]} euros")

achats = Achats()

while True:
    cmd = input("Commande : (+ : ajouter des produits), (s : supprimer), (t : afficher le prix total), (a : afficher la liste des produits) (q : quitter)")

    if cmd == "+":
        produit = input("Entrez le nom du produit: ")
        prix = float(input("Entrez le prix du produit: "))
        achats.ajouter(produit, prix)
    elif cmd == "s":
        produit = input("entrez le nom du produit: ")
        achats.supprimer(produit)
    elif cmd == "t":
        achats.prix_total()
    elif cmd == "a":
        achats.afficher()
    elif cmd == "q":
        break
    else:
        print("commande invalide")
