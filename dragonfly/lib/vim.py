""" Module vim

This module contains vim commands.

Author: Simon Larsen
Version: 2016-06-02

"""
import format

from dragonfly import (
    Function,
    MappingRule,
    Integer,
    Grammar,
    Dictation,
    Choice,
    Key,
    Text
)

def insertion(insert):
    Key(str(insert)).execute()

class MainRule(MappingRule):
    # Different points of insertion
    insert_points = {
    "before": "i",
    "at home": "I",
    "after": "a",
    "at end": "A",
    "above": "O",
    "below": "o",
    }

    mapping = {
    "[use] insert [<insert>]": Function(insertion, extra = {"insert"}),
    }
    extras = [
        Dictation("text"),
	Choice("insert", insert_points),
    ]
    defaults = {
    "insert": "i",
    }


# Load and disable grammar
grammar = Grammar("vim")
grammar.add_rule(MainRule())
grammar.load()
grammar.disable()

def enable():
    global grammar
    if not grammar.enabled:
        grammar.enable()

def disable():
    global grammar
    if grammar.enabled:
        grammar.disable()
