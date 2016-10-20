"""
This module contains voice commands for formatting Markdown.

Author: Simon Larsen
Version: 2016-10-20
"""

from dragonfly import ( Key, Function, Grammar, Dictation, MappingRule,
                        Text, Choice, Integer )

from lib import(format)

class FormatRule(MappingRule):
    """ This is the main rule for the Markdown module.
    It contains all of the formatting commands. """

    languages = {
    }

    mapping = {
        "header <i>": Key("hash:%(i)d"),
    }
    extras = [
        Dictation("text"),
        Choice("language", languages),
        Integer("i", 1, 6),
    ]

# load and disable the grammar
grammar = Grammar("markdown")
grammar.add_rule(FormatRule())
grammar.load()
grammar.disable()

# Functions that enable and disable this grammar
def enable():
    global grammar
    if not grammar.enabled:
        grammar.enable()

def disable():
    global grammar
    if grammar.enabled:
        grammar.disable()
