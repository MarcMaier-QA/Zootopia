# wenn es ein tier nicht gibt bekommen wir [] zurück

import requests

API_KEY = "3YVnDWrvMPeTKxic/mWOJA==c4MjPJpK2cD9qF9Q"

def fetch_animals(animal_name: str):
    """
    Fetches animal dara from the Animals API using the provided animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of dictionaries containing animal information.
        Returns an empty list if no animals are found or if an error occurs.
    """
    # Construct the API endpoint with the animal name
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

    # set the header with the API key
    headers = {"X-Api-Key": API_KEY}

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []


animals = fetch_animals("Fox")
print(animals)