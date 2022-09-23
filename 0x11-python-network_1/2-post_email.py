#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        mail = response.read().decode(encoding='UTF-8')
        print(mail)
