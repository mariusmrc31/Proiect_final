import requests

from requests_folder.get_token import token


def get_an_order(order_id):
    header_params = {'Authorization': token}
    response = requests.get(f"https://simple-books-api.glitch.me/orders/{order_id}",
                            headers=header_params)
    return response
