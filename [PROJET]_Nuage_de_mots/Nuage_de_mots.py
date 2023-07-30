import json

with open('[PROJET]_Nuage_de_mots/fichier.txt', encoding = 'utf-8') as f:
    ligne = f.read().splitlines()
    mots = ' '.join(ligne).split(' ')
    
    nuage_mots={}
    exclure = ['de', 'et', 'est', 'un', 'la', 'le', 'une', 'Il', 'il', '', 'à']
    for m in mots:
        if m in exclure:
            continue
        if m in nuage_mots:
            nuage_mots[m] +=1
        else:
            nuage_mots[m]= 1
    nuage_mots = dict(sorted(nuage_mots.items(),key=lambda item:item[1],reverse=True))
    print(nuage_mots)

with open('[PROJET]_Nuage_de_mots/nuage_mots.json','w',encoding='utf-8') as fw:
    json.dump(nuage_mots, fw, ensure_ascii=False)