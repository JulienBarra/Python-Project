nom_complet = "julien barra"
nom_complet_liste = nom_complet.split(" ")

initiales = nom_complet_liste[0][0] + nom_complet_liste[1][0]
initiales = initiales.upper()

print(f"Les initiales de {nom_complet} sont {initiales}")