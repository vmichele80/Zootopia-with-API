Animal Website Generator

This project generates a simple HTML page with “animal cards” based on an animal name you enter.
It fetches animal data from the API Ninjas Animals API, injects the results into an HTML template, and writes the final page to animals.html.

Installation

Install dependencies:
pip install -r requirements.txt


Add your API key (recommended approach):
Create a .env file in the project root

Add:
API_KEY=your_api_ninjas_key_here


Usage

Make sure animals_template.html exists in the project root (this file is used as the template).

Run the script:
python animals_web_generator.py


When prompted, type an animal name (example: fox, tiger, elephant).

The script will generate:
animals.html — your final webpage

You should see:
A set of animal cards if results are found
Or an error message on the page if no animal matches

Output

Generated file: animals.html
Template file required: animals_template.html
The template must contain the placeholder:
__REPLACE_ANIMALS_INFO__
This placeholder gets replaced with the generated animal cards.


Project Structure

animals_web_generator.py — prompts the user, fetches animal data, generates the final HTML
data_fetcher.py — calls the API Ninjas endpoint and returns JSON data
animals_template.html — HTML template containing __REPLACE_ANIMALS_INFO__
animals.html — generated output file (created after running)
