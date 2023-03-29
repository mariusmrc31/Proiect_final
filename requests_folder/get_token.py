import requests
import random


def generate_token():
    nr = random.randint(1, 99999999999)
    nr1 = random.randint(1, 99999999999)
    request_body = {
                   "clientName": "Marius Marcu",
                   "clientEmail": f"marius{nr}.marcu{nr1}@example.com"
                   }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=request_body)
    # am generat token ul si vrem sa l extragem din raspuns
    token = response.json()["accessToken"]  # scriem .json() ca sa extragem tot raspunsul
    return token


token = generate_token()
