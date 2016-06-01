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
        "if": Text("if () {") + Key("enter:2") + Text("}"),
	}

