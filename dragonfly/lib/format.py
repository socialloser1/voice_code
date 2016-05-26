'''Module format

This module contains general formatting functions.

Author: Simon Larsen
Version: 2016-05-26

'''


''' Takes a string input and returns the same string
with snake case formatting.

'''
def snake_case( text ):
    new_text = ""
    words = str(text).split()
    for word in words:
        if new_text != "" and new_text[-1:].isalnum() and word[-1:].isalnum():
            word = "_" + word
        new_text += word.lower()
    return new_text