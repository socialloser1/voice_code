'''Module format

This module contains general formatting functions.

Author: Simon Larsen
Version: 2016-05-26

'''


''' Takes a string parameter and returns the same string
with snake case formatting.

'''
def snake_case( text ):
    new_text = ""
    words = str( text ).split()
    for word in words:
        if new_text != "" and new_text[-1:].isalnum() and word[-1:].isalnum():
            word = "_" + word
        new_text += word.lower()
    return new_text

''' Takes a string parameter and returns the same string
with camel case formatting
'''
def camel_case( text ):
    new_text = ""
    text = str( text ).lower()
    cap_next = False

    for char in text:
        if char == " " :
            cap_next = True
        elif cap_next:
            new_text += char.upper()
            cap_next = False
        else:
            new_text += char
    return new_text

''' Takes a string parameter and returns the same string
with pascal case formatting
'''
def pascal_case( text ):
	# Camel case and cap the first letter
	new_text = camel_case( text )
	return str( new_text[0].upper() ) + str( new_text[1:] )

''' Takes a string parameter and returns it in all
lowercase without white spaces
'''
def no_space_lower( text ):
	new_text = ""
	for word in str( text ).lower().split():
		new_text += word
	return new_text

''' Takes a string parameter and returns it in all
uppercase without white spaces
'''
def no_space_upper( text ):
	new_text = ""
	for word in str( text ).upper().split():
		new_text += word
	return new_text
