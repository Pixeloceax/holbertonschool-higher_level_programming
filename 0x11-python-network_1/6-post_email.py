#!/usr/bin/python3
"""
    sends a POST request to the passed URL with the email as a parameter,
"""

import requests
import urllib.parse
from sys import argv
import urllib.request

if __name__ == "__main__":

    email = requests.post(argv[1], data={'email': argv[2]})
    print(email.text)
