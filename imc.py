poids = float(input("Votre poids est (Kg) "))
taille = float(input("Votre taille est (m) "))

imc = poids/(taille**2)

print(f"L'IMC d'une personne de {poids} kg et {taille} m est {imc} Kg/m^2.")