#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        var = {"q":""}
    else:
        var = {"q":sys.argv[1]}
    response = requests.post("http://0.0.0.0:5000/search_user", data=var)
    try:
        result = response.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
