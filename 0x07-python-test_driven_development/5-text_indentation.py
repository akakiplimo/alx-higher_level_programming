#!/usr/bin/python3
"""
This is a module with one function text_indentation(text)
"""
def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '.' or a == '?' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
