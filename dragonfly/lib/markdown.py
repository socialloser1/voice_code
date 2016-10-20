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
        "python": "python",
        "java": "java",
        "bash": "bash",
        "prolog": "prolog",
        "haskell": "haskell",
        "vanilla": "",
    }

    mapping = {
        "header <i>": Key("hash:%(i)d"),
        "horz": Key("hyphen:3"),
        "code block <language>": Key("backtick:3") + Text("%(language)s") + Key("enter, backtick:3, up, end, enter"),
        "emph [<text>]": Key("underscore:2, left:1") + Text("%(text)s"),
        "bold [<text>]": Key("asterisk:4, left:2") + Text("%(text)s"),
        "insert image": Key("exclamation, lbracket, rbracket, lparen, rparen, left:3"),
        "insert link": Key("lbracket, rbracket, lparen, rparen, left:3"),
    }
    extras = [
        Dictation("text"),
        Choice("language", languages),
        Integer("i", 1, 6),
    ]
    defaults = {
        "text": "",
    }

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
