#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -i $1 | grep Content-Length | tail -c 4
