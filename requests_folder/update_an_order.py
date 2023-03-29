import requests

from requests_folder.get_token import token


def update_an_order(customerName, orderId):
    request_body = {
        "customerName": customerName
    }

    header_params = {'Authorization': token}
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{orderId}", json=request_body, headers=header_params)
    return response
