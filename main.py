# wenn es ein tier nicht gibt bekommen wir [] zurück

import requests

api_key = "3YVnDWrvMPeTKxic/mWOJA==c4MjPJpK2cD9qF9Q"

animal_name = "tiger"

url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

headers = {
    "X-Api-Key": api_key
}

# GET Request senden
response = requests.get(url, headers=headers)

# Prüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    data = response.json()  # JSON in Python dict umwandeln
    print(data)
else:
    print(f"Fehler: {response.status_code}, {response.text}")