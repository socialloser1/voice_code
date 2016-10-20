"""
This module contains voice commands for formatting Markdown.

Author: Simon Larsen
Version: 2016-10-20
"""

from dragonfly import ( Key, Function, Grammer, Dictation, MappingRule,
                        Text, Choice, Integer )

from lib import(format)

class FormatRule(MappingRule):
    """ This is the main rule for the Markdown module.
    It contains all of the formatting commands. """

    mapping = [
    ]
    extras = [
        Dictation("text"),
        Choice("language", languages),
        Integer("i", 0, 10),
    ]

grammar = Grammar("markdown")
grammar.add_rule(FormatRule())
grammar.load()
