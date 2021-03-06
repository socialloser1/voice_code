"""Module format

This module contains general formatting functions.

Author: Simon Larsen
Version: 2016-05-26

"""

# the current year
year = 16

# A mapping of months to numbers
months = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "october": "10",
        "november": "11",
        "december": "12",
        }

""" Takes a string parameter and returns the same string
with snake case formatting.

"""
def snake_case( text ):
    new_text = ""
    words = str( text ).split()
    for word in words:
        if new_text != "" and new_text[-1:].isalnum() and word[-1:].isalnum():
            word = "_" + word
        new_text += word.lower()
    return new_text

""" Takes a string parameter and returns the same string
with camel case formatting
"""
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

""" Takes a string parameter and returns the same string
with pascal case formatting
"""
def pascal_case( text ):
	# Camel case and cap the first letter
	new_text = camel_case( text )
	return str( new_text[0].upper() ) + str( new_text[1:] )

""" Takes a string parameter and returns it in all
lowercase without white spaces
"""
def no_space_lower( text ):
	new_text = ""
	for word in str( text ).lower().split():
		new_text += word
	return new_text

""" Takes a string parameter and returns it in all
uppercase without white spaces
"""
def no_space_upper( text ):
	new_text = ""
	for word in str( text ).upper().split():
		new_text += word
	return new_text

""" Concatenates the first letter of every word in the parameter and
returns them as lowercase.
"""
def lowercase_letters( text ):
    new_text = ""
    words = text.split()
    for current in words:
        new_text += current[0]
    return new_text.lower()

""" Concatenates the first letter of every word in the parameter and
returns them as uppercase.
"""
def uppercase_letters( text ):
    return lowercase_letters(text).upper()

def format_date(month, day):
    """ Formats the input month and day 2016 """
    global year
    print "success"
    return "%d-%s-%d"%(year, month, day)

