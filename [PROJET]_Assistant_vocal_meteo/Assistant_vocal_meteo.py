import requests
import pyttsx4

engine = pyttsx4.init()
engine.setProperty('voice', '')

ville = "Bordeaux"
#Si vous voulez tester le code, il vous faut rentrer votre clé API ci dessous
api_key = "........"

try:
    reponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric")
    status_code =reponse.status_code
    
    if status_code == 200:
        donnees = reponse.json()
        #Température / Ressenti / Description du temps / Humidité
        temperature = donnees["main"]["temp"]
        ressenti = donnees["main"]["feels_like"]
        description = donnees["weather"][0]["description"]
        humidite = donnees["main"]["humidity"]
        print(f"{ville} - Température: {temperature} C°, Ressenti: {ressenti} C°, Description: {description}, Humidité: {humidite}%")
        engine.say(f"{ville} - Température: {temperature} degré celsius, Ressenti: {ressenti} degré celsius, Humidité: {humidite}%")
        engine.runAndWait()
        
    else:
        print("Erreur lors de la récupération des données...")

except Exception as e:
    print("Une erreur s'est produite: ", e)
