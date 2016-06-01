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
    IntegerRef,
    Grammar,
    Dictation,
    Key,
    Text
)

""" Creates an empty doc string

As of right now, this function is not working properly!
"""
def doc_string():
    Text('" " " " " " ').execute()
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

""" Outputs 'text' = 'i', where multiple words in 'text' are snake-cased."""
def assign_int(text, i):
    Text(format.snake_case(str(text))  + " = " + str(i)).execute()

""" Outputs a for-each loop with the input parameter as the collection
to iterate over. If the parameter consists of several words, it will be snake-cased 
"""
def for_each(text):
    coll = format.snake_case(str(text))
    Text("for current in %s:"%(coll)).execute()
    Key("enter").execute()

""" The MappingRule for this module."""
class MainRule( MappingRule ):

	mapping = { 
        '[use] defunc <text>': Function(def_function, extra = {"text"}),
        '[use] pydoc': Function(doc_string),
        '[use] class <text>': Function(def_class, extra = {"text"}),
        '[use] assign <text> integer [<i>]': Function(assign_int, extra={"text", "i"}),
        '[use] for range [<i>]': Text("for i in range(0, %(i)d):"),
        '[use] for each <text>': Function(for_each, extra = {"text"}),
	    'doc string': Function(doc_string),

        # Keywords
        'for': Text("for"),
        'else': Text("else:") + Key("enter"),
        'if': Text("if :") + Key("left"),
        'elif': Text("elif :") + Key("left"),
        'import': Text("import "),
        'test if': Text("if () {") + Key("enter:2") + Text("}"),
	}
	extras = [
                Dictation("text"),
                Integer("i", 0, 10000),
	]
	defaults = {
                "i": 0,
    }

# Load and disable grammar
grammar = Grammar('python')
grammar.add_rule(MainRule())
grammar.load()
grammar.disable()

def enable():
    global grammar
    if grammar.enabled == False:
        grammar.enable()

def disable():
    global grammar
    if grammar.enabled:
        grammar.disable()