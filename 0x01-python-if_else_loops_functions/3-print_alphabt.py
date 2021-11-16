#!/usr/bin/python3
# Prints the ASCII alphabet, in lowercase, not followed by a new line
for letter in range(97, 123):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print("{}".format(chr(letter)), end = "")

