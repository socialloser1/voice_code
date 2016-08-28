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

def equals_variable(text):
    Text(" = %s;"%(format.snake_case(text))).execute()

def gcc(text):
    Text("gcc --std=c99 %s -o %s"%(format.snake_case(text) + ".c", format.snake_case(text))).execute()

def scan(data_type, i):
    string = 'scanf("'

    for x in range(i-1):
        string += "%" + "%s, "%(data_type)

    string += "%" + '%s"'%(data_type)

    # Append the pointer "placements"
    for x in range(i):
        string += ", "

    # Finish the string and print
    string += ");"
    Text(string).execute()

    # Place cursor
    steps = 2 + (i-1)*2
    Key("left:%d"%(steps)).execute()


""" MappingRule for keywords """
class KeywordsRule(MappingRule):
    common_packages = {
        "standard i oh": "stdio",
        "standard bool": "stdbool",
        "assert": "assert",
        "see type": "ctype",
        "error": "errno",
        "float": "float",
        "limits": "limits",
        "locale": "locale",
        "math": "math",
        "set jump": "setjmp",
        "signal": "signal",
        "standard argument": "stdarg",
        "standard definition": "stddef",
        "standard library": "stdlib",
        "string": "string",
        "time": "time",
    }

    # For scanning and printing
    data_types = {
        "integer": "d",
        "float": "f",
        "character": "c",
        "string": "s",
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
        "for": Text("for () {") + Key("enter, rbrace, up, end, left:3"),
        "for range <i> increment": Text("for (int i = 0; i < %(i)s; i++) {}")
        + Key("left, enter, up, end, enter"),
        "for range <i> decrement": Text("for (int i = %(i)s; 0 <= i; i--) {}")
        + Key("left, enter, up, end, enter"),
        "include": Text("#include <>") + Key("left"),
        "include <package>": Text("#include <%(package)s.h>"),
        "define": Text("#define "),
        "print": Text("printf();") + Key("left:2"),
        "print string": Text('printf("\\n");') + Key("left:5"),
        "scan <data_type> <i>": Function(scan, extra = {"data_type", "i"}),
        "return": Text("return ;") + Key("left"),
        "return <boolean_int>": Text("return %(boolean_int)d;"),
        "ekint <i>": Text(" = %(i)d;"),
        "eknegint <i>": Text(" = -%(i)d;"),
        "ekvar <text>": Function(equals_variable, extras = {"text"}),
        "integer": Text("int"),
        "float": Text("float"),
        "double": Text("double"),
        "character": Text("char"),
        "true": Text("true"),
        "false": Text("false"),
        "compile see code <text>": Function(gcc, extra = {"text"}),
    }
    extras = [
        Choice("package", common_packages),        
        Choice("boolean_int", boolean_ints),
        Integer("i", 0, 10000),
        Dictation("text"),
        Choice("data_type", data_types),
    ]

""" Below is is everythong needed to declare functions, classes and variables """
def declare_variable_mod(modifier, data_type, text):
    text = format.snake_case(text)
    if modifier == None or modifier == "":
        declaration = "%s %s;"%(data_type, text)
    else:
        declaration = "%s %s %s;"%(modifier, data_type, text)
    
    Text(declaration).execute()

def declare_pointer(data_type, text):
    declare_variable_mod(None, data_type, "*%s"%(text))

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

def pointer_to(text):
    Text("&%s"%(format.snake_case(text))).execute()

def deref_pointer(text):
    Text("*%s"%(format.snake_case(text))).execute()

class VariablesRule(MappingRule):

    data_types = {
            "integer": "int",
            "float": "float",
            "character": "char",
            "double": "double",
            "void": "void",
            "short": "short",
            "long": "long",
            "signed": "signed",
            "unsigned": "unsigned",
            "boolean": "bool",
    }

    mapping = {
            "declare <text> as <data_type>": Function(declare_variable, extra = {"data_type", "text"}),
            "declare <text> as <data_type> pointer": Function(declare_pointer, extra = {"data_type", "text"}),
            "short <text> as <data_type>": Function(declare_short, extra = {"data_type", "text"}),
            "long <text> as <data_type>": Function(declare_long, extra = {"data_type", "text"}),
            "signed <text> as <data_type>": Function(declare_signed, extra = {"data_type", "text"}),
            "unsigned <text> as <data_type>": Function(declare_unsigned, extra = {"data_type", "text"}),
            "defunc <text> return <data_type>": Function(define_function, extra = {"data_type", "text"}),
            "pointer to <text>": Function(pointer_to, extra = {"text"}),
            "deref <text>": Function(deref_pointer, extra = {"text"}),
            "size of <text>": Text("sizeof(%(variable)s)"),
            "size of": Text("sizeof()") + Key("left"),
            "type <data_type>": Text("%(data_type)s"),
            "cast <data_type>": Text("(%(data_type)s)"),
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
