# animals_web_generator.py
"""
Main module for generating an animal website.
"""

import data_fetcher

def generate_website(animals, animal_name):
    """
    Generates an HTML file displaying information about the animals.
    If no animal are found displays a friendly error message.

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
        html_content += f"<h2 style='color:red;'>The animal '{animal_name}' doesn't exist.</h2>"
        html_content += "<p>Please try another animal name.</p>"

    html_content += "</body></html>"

    # Save HTML to file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html")


# Main program
if __name__ == "__main__":
    # Ask user for animal input
    user_input = input("Enter a name of an animal: ").strip()

    # Fetch animal data
    animals = data_fetcher.fetch_data(user_input)

    # Generate website
    generate_website(animals, user_input)