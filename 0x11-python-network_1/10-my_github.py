#!/usr/bin/python3
"""
    Write a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    pwd = argv[2]
    request = requests.get('https://api.github.com/user', auth=(user, pwd))
    print(request.json().get("id"))
