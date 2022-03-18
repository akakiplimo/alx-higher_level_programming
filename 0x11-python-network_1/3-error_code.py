#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import urllib
from urllib import request
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        request.urlopen(req)
        with request.urlopen(req) as response:
            resp = response.read().decode('utf-8')
            print(resp)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
        
