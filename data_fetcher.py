import requests
import os
from dotenv import load_dotenv



URL_REQUEST = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = os.getenv('API_KEY')



def fetch_data(animal_name):
    """This function fetch the data via API"""
    load_dotenv()
    res = requests.get(f"{URL_REQUEST}{animal_name}", headers={"X-Api-Key":"Bn6bsORJmnFmjtA7f4EWvZdHKKzSl8CgrqNcKebx"})
    res = res.json()
    return res


if __name__ == '__main__':
    main()