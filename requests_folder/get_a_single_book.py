import requests


def get_a_single_book(bookid):
    response = requests.get(f"https://simple-books-api.glitch.me/books/{bookid}")
    return response
