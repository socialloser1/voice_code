'''Module py_lang

This module contains general formatting for the Python language.

Author: Simon Larsen
Version: 2016-05-27

'''
import format

from dragonfly import (
    Function,
    MappingRule,
    IntegerRef,
    Grammar,
    Dictation,
    Key,
    Text
)

''' Creates an empty doc string

As of right now, this function is not working properly!
'''
def doc_string():
    Text("''''''").execute()
    Key("left:3").execute()

''' Function that prints out a Python function definition,
with the parameter text as the function name.
'''
def def_function(text):
    Text("def " + format.snake_case(str(text)) + "():").execute()
    Key("left:2").execute()

class MainRule( MappingRule ):

	mapping = { 
        '[use] def pyfunc [<text>]': Function(def_function, extra = {"text"}),
        '[use] pydoc': Function(doc_string),
	}
	extras = [
                Dictation( "text" ),
	]
	defaults = {"text": "",
    }

grammar = Grammar('python')
grammar.add_rule(MainRule())
grammar.load()

