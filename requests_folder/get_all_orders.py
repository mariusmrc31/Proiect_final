import requests

from requests_folder.get_token import token


def get_all_orders():
    header_params = {'Authorization': token}
    response = requests.get("https://simple-books-api.glitch.me/orders", headers=header_params)
    return response
