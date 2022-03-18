#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
