#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
"""
import urllib.request
import urllib.parse
from sys import argv
from urllib.error import HTTPError
import requests

if __name__ == "__main__":

    request = requests.get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
