import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL_REQUEST = "https://api.api-ninjas.com/v1/animals?name="
api_key = os.getenv('API_KEY')


def fetch_data(animal_name):

    """This function fetch the data via API"""
    res = requests.get(f"{URL_REQUEST}{animal_name}", headers={"X-Api-Key": api_key})
    res = res.json()
    return res


if __name__ == '__main__':
    main()