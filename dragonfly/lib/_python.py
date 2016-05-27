'''Module py_lang

This module contains general formatting for the Python language.

Author: Simon Larsen
Version: 2016-05-27

'''
import format

from dragonfly import (
    Function,
    MappingRule,
    Integer,
    Grammar,
    Dictation,
    Key,
    Text
)

""" Creates an empty doc string

As of right now, this function is not working properly!
"""
def doc_string():
    Text('""""""').execute()
    Key("left:3").execute()

""" Function that prints out a Python function definition,
with the parameter text as the function name.
"""
def def_function(text):
    Text("def " + format.snake_case(str(text)) + "():").execute()
    Key("left:2").execute()

""" Outputs a class definition with the parameter
text as the class name.
"""
def def_class(text):
    Text("class " + format.pascal_case(str(text)) + "():").execute()
    Key("left:2").execute()

""" Outputs 'text' = 'n', where multiple words in 'text' are snake-cased.
"""
def assignment(text, n):
    Text(format.snake_case(str(text))  + " = " + str(n)).execute()

""" The MappingRule for this module."""
class MainRule( MappingRule ):

	mapping = { 
        '[use] defunc [<text>]': Function(def_function, extra = {"text"}),
        '[use] pydoc': Function(doc_string),
        '[use] class [<text>]': Function(def_class, extra = {"text"}),
        '[use] assign [<n>] to [<text>]': Function(assignment, extra={"text","n"}),
	}
	extras = [
                Dictation("text"),
                Integer("n", 0, 10000),

	]
	defaults = {"text": "",
                "n": 0,
    }

grammar = Grammar('python')
grammar.add_rule(MainRule())
grammar.load()

