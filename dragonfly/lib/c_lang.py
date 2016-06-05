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
    Text
)


""" MappingRule for keywords """
class KeywordsRule(MappingRule):
	mapping = {
                "if": Text("if () {") + Key("enter:2") + Text("}") + Key("up:2, end, left:3"),
                "else if": Text("else if () {") + Key("enter:2") + Text("}")
                + Key("up:2, end, left:3"),
                "else": Text("else {}") + Key("left, enter, up, end, enter"),
	}

# Load and disable grammar
grammar = Grammar("c")
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
