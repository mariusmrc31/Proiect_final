import requests

from requests_folder.get_token import token


def post_submit_an_order(bookid, customerName):
    body_request = {
        "bookId": bookid,
        "customerName": customerName
    }

    header_params = {'Authorization': token}
    response = requests.post("https://simple-books-api.glitch.me/orders", json=body_request,
                             headers=header_params)
    return response
