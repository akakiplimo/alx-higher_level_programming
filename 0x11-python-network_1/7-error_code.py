#!/usr/bin/python3
"""
Script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
from requests import exceptions
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        req.raise_for_status()
        print(req.text)
    except exceptions.HTTPError as e:
        print("Error code: {}".format(req.status_code))
