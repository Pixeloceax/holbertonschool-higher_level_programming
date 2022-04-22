#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable X-Request-Id
"""

import requests
from sys import argv

if __name__ == "__main__":

    html = requests.get(argv[1])
    print(html.headers.get('X-Request-Id'))
