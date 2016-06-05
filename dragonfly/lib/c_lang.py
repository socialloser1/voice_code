""" Module c_lang

This module contains general formatting for the Python language.

Author: Simon Larsen
Version: 2016-05-31

"""

import format

from dragonfly import (
    Function,
    MappingRule,
    Integer,
    IntegerRef,
    Grammar,
    Dictation,
    Key,
    Text,
    Choice
)


""" MappingRule for keywords """
class KeywordsRule(MappingRule):
    mapping = {
            "if": Text("if () {") + Key("enter:2") + Text("}") + Key("up:2, end, left:3"),
            "else if": Text("else if () {") + Key("enter:2") + Text("}")
            + Key("up:2, end, left:3"),
            "else": Text("else {}") + Key("left, enter, up, end, enter"),
    }

def declare_variable(modifier, data_type, text):
    if modifier == None or modifer == "":
        declaration + "%s %s"%(data_type, text)
    else:
        declaration + "%s %s %s"%(modifier, data_type, text)
    
    Text(declaration).execute()

def test(text, data_type):
    Text("%s %s;"%(data_type, text)).execute()

class VariablesRule(MappingRule):

    data_types = {
            "integer": "int",
            "float": "float",
            "char": "char",
            "double": "double",
    }

    mapping = {
            "declare <text> as <data_type>": Function(test, extra = {"text", "data_type"}),
    }
    extras = [
            Choice("data_type", data_types),
            Dictation("text"),
            Integer("n", 1, 10),
    ]
    defaults = {
            "n": 5,        
    }

# Load and disable grammar
grammar = Grammar("c")
grammar.add_rule(VariablesRule())
grammar.add_rule(KeywordsRule())
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
