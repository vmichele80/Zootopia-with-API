import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_html():
    fname = 'animals_template.html' #this html file is stored on the same folder of the code file
    html_file = open(fname, 'r')
    source_code = html_file.read()
    return source_code

def animals_cards(animals_data):
    output = ''
    for animal in animals_data:
        characteristics = animal["characteristics"]
        output += "<li>"
        output += f"Name: {animal["name"]}\n"
        output += f"Diet: {characteristics["diet"]}\n"
        output += f"Location: {animal["locations"][0]}\n"
        if "type" in characteristics:
            output += f"Type: {characteristics["type"]}\n"
        output += "</li>"
    return output

def main():
    animals_data = load_data('animals_data.json')
    html_code = load_html()

    animals_list = animals_cards(animals_data)

    new_html_code = html_code.replace("__REPLACE_ANIMALS_INFO__", animals_list)
    # print(new_html_code)
    with open("animals.html", "a") as f:
        f.write(new_html_code)

if __name__ == '__main__':
    main()