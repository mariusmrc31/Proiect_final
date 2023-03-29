import requests

from requests_folder.get_token import token


def delete_an_order(orderId):
    header_params = {'Authorization': token}
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{orderId}",
                               headers=header_params)
    return response
