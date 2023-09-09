import requests

from dotenv import load_dotenv
import os

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USER_ENDPOINT = os.getenv("SHEETY_USER_ENDPOINT")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_user_data(self):
        user_email = []
        response = requests.get(url=SHEETY_USER_ENDPOINT)
        data = response.json()
        user_data = data["users"]
        for item in user_data:
            email = item['email']
            user_email.append(email)
        return user_email


dm = DataManager()
print(dm.get_user_data())
