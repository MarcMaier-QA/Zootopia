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

def generate_website(animals, animal_name):
    """
    Generates an HTML file displaying information about the animals.

    Args:
        animals (list): List of animal dictionaries from the API.
        animal_name (str): The name of the animal queried.
    """
    html_content = "<html><head><title>Animals</title></head><body>"

    if animals:
        html_content += f"<h1>Results for '{animal_name}'</h1>"
        for animal in animals:
            html_content += "<div style='margin-bottom:20px;'>"
            html_content += f"<h2>{animal.get('name', 'Unknown')}</h2>"
            html_content += f"<p>Latin Name: {animal.get('latin_name', 'Unknown')}</p>"
            html_content += f"<p>Type: {animal.get('animal_type', 'Unknown')}</p>"
            html_content += f"<p>Active Time: {animal.get('active_time', 'Unknown')}</p>"
            html_content += f"<p>Length: {animal.get('length_min', '?')} - {animal.get('length_max', '?')} ft</p>"
            html_content += f"<p>Weight: {animal.get('weight_min', '?')} - {animal.get('weight_max', '?')} lbs</p>"
            html_content += f"<p>Lifespan: {animal.get('lifespan', '?')} years</p>"
            html_content += f"<p>Habitat: {animal.get('habitat', 'Unknown')}</p>"
            html_content += f"<p>Diet: {animal.get('diet', 'Unknown')}</p>"
            html_content += "</div>"
    else:
        html_content += f"<h2>The animal '{animal_name}' doesn't exist.</h2>"

    html_content += "<body></html>"

    # Save HTML to file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html")


# Main program
if __name__ == "__main__":
    # Ask user for animal input
    user_input = input("Enter a name of an animal").strip()

    # Fetch animal data
    animals = fetch_animals(user_input)

    # Generate website
    generate_website(animals, user_input)