import json
import requests

URL_REQUEST = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "Bn6bsORJmnFmjtA7f4EWvZdHKKzSl8CgrqNcKebx"
ANIMAL = "FOX"
URLS_REQUEST_COMPLETE = URL_REQUEST + ANIMAL

def fetch_animal_json(URL_REQUEST):
    """This function fetch the data via API"""
    res = requests.get(URL_REQUEST, headers={"X-Api-Key":"Bn6bsORJmnFmjtA7f4EWvZdHKKzSl8CgrqNcKebx"})
    res = res.json()
    print(res)

def load_data(file_path):
    """it loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def load_html():
    """it loads a the HTML code from the template"""
    with open("animals_template.html", "r", encoding="utf-8") as fname:
        source_code = fname.read()
    return source_code


def animals_cards(animals_data):
    """it generates all the animal cards"""
    output = ''  # define an empty string
    for animal in animals_data:
        # append information to each string
        characteristics = animal["characteristics"]
        output += '<li class="cards__item">'
        output += f'<div class="card__title"> {animal["name"]}</div>\n'
        output += '<div class ="card__text" >\n<ul>'
        output += f'<li><strong>Diet: </strong>{characteristics["diet"]}</li>\n'
        output += f'<li><strong>Location: </strong>{animal["locations"][0]}</li>\n'
        if "type" in characteristics:
            output += f'<li><strong>Type: </strong>{characteristics["type"]}</li>\n'
        output += '</ul>\n</div>\n</li>'
    return output

def main():
    fetch_animal_json(URLS_REQUEST_COMPLETE)
    # animals_data = load_data('animals_data.json')
    # html_code = load_html()
    # animals_list = animals_cards(animals_data)
    # new_html_code = html_code.replace("__REPLACE_ANIMALS_INFO__", animals_list)

    # with open("animals.html", "w", encoding="utf-8") as f:  # Write the new html code to a file
        #f.write(new_html_code)

if __name__ == '__main__':
    main()