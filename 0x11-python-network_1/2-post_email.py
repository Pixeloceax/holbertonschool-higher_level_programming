#!/usr/bin/python3
"""
    sends a POST request to the passed URL with the email as a parameter,
"""

import urllib.parse
from sys import argv
import urllib.request


if __name__ == "__main__":

    email = {'email': argv[2]}
    value = urllib.parse.urlencode(email).encode('ascii')
    post = urllib.request.Request(argv[1], value)
    with urllib.request.urlopen(post) as response:
        print(response.read().decode('utf-8'))
