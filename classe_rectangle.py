class Rectangle :
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
#Calcul du périmètre du rectangle
    def Perimetre(self):
        return 2*(self.longueur+self.largeur)
    
#Calcul de la surface du rectangle
    def Surface(self):
        return self.longueur*self.largeur
    
#On veut savoir si finalement le rectangle n'est pas un carré
    def est_carre (self):
        if self.longueur == self.largeur :
            return True
        else:
            return False
        

Monrectangle = Rectangle (6,6)

print(f"Le périmètre de mon rectangle est égale à {Monrectangle.Perimetre()} m")
print(f"La surface de mon rectangle est égale à {Monrectangle.Surface()} m^2")
print(f"Mon rectangle est enfait un carré ? : {Monrectangle.est_carre()}")