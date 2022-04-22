#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
"""
import urllib.request
import urllib.parse
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
