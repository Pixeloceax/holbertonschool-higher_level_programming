#!/usr/bin/python3
"""
    Write a Python script that takes in a letter
    and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) <= 1:
        q = ""
    else:
        q = argv[1]

    request = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = request.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
