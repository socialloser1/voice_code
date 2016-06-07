""" Module c_lang

This module contains general formatting for the Python language.

Author: Simon Larsen
Version: 2016-05-31

"""

import format
from general_programming import SymbolsRule

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
    common_packages = {
        "standard i oh": "stdio.h",
        "standard bool": "stdbool.h",
    }

    boolean_ints = {
        "True": 1,
        "False": 0,
    }

    mapping = {
        "if": Text("if () {") + Key("enter") + Text("}") + Key("up, end, left:3"),
        "else if": Text("else if () {") + Key("enter") + Text("}")
        + Key("up, end, left:3"),
        "else": Text("else {}") + Key("left, enter, up, end, enter"),
        "while": Text("while () {") + Key("enter, rbrace, up, end, left:3"),
        "for": Text("for ()  {") + Key("enter, rbrace, up, end, left:3"),
        "for range <i> increment": Text("for (int i = 0, i < %(i)s, i++) {}")
        + Key("left, enter, up, end, enter"),
        "for range <i> decrement": Text("for (int i = %(i)s, 0 <= i, i--) {}")
        + Key("left, enter, up, end, enter"),
        "include": Text("#include <>") + Key("left"),
        "include <package>": Text("#include <%(package)s>"),
        "define": Text("#define "),
        "print": Text("printf();") + Key("left:2"),
        "print string": Text('printf("\\n");') + Key("left:5"),
        "return": Text("return ;") + Key("left"),
        "return <boolean_int>": Text("return %(boolean_int)d;"),
    }
    extras = [
        Choice("package", common_packages),        
        Choice("boolean_int", boolean_ints),
        Integer("i", 0, 10000),
    ]

""" Below is is everythong needed to declare functions, classes and variables """
def declare_variable_mod(modifier, data_type, text):
    text = format.snake_case(text)
    if modifier == None or modifier == "":
        declaration = "%s %s;"%(data_type, text)
    else:
        declaration = "%s %s %s;"%(modifier, data_type, text)
    
    Text(declaration).execute()

def declare_variable(data_type, text):
    declare_variable_mod(None, data_type, text)

def declare_short(data_type, text):
    declare_variable_mod("short", data_type, text)

def declare_long(data_type, text):
    declare_variable_mod("long", data_type, text)

def declare_signed(data_type, text):
    declare_variable_mod("signed", data_type, text)

def declare_unsigned(data_type, text):
    declare_variable_mod("unsigned", data_type, text)

def define_function(data_type, text):
    Text("%s %s() {"
            %(data_type, format.snake_case(text))).execute()
    Key("enter, rbrace, up, end, left:3").execute()

class VariablesRule(MappingRule):

    data_types = {
            "integer": "int",
            "float": "float",
            "character": "char",
            "double": "double",
    }

    mapping = {
            "declare <text> as <data_type>": Function(declare_variable, extra = {"data_type", "text"}),
            "short <text> as <data_type>": Function(declare_short, extra = {"data_type", "text"}),
            "long <text> as <data_type>": Function(declare_long, extra = {"data_type", "text"}),
            "signed <text> as <data_type>": Function(declare_signed, extra = {"data_type", "text"}),
            "unsigned <text> as <data_type>": Function(declare_unsigned, extra = {"data_type", "text"}),
            "defunc <text> return <data_type>": Function(define_function, extra = {"data_type", "text"}),
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
grammar.add_rule(SymbolsRule())
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
