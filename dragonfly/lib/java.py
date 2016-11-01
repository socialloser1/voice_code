""" Module java

This module contains general formatting for the Java language.

Author: Simon Larsen
Version: 16-09-01

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


""" MappingRule for keywords """
class KeywordsRule(MappingRule):
    common_packages = {
            "hash set": "java.util.HashSet",
            "hash map": "java.util.HashMap",
            "array list": "java.util.ArrayList",
            "list": "java.util.List",
            "scanner": "java.util.scanner",
            "random": "java.util.Random;"
    }

    mapping = {
        "if": Text("if ") + Key("lparen, rparen, space, lbrace, enter, rbrace, up, end, left:3"),
        # "if": Text("if () {") + Key("enter") + Text("}") + Key("up, end, left:3"),
        "else if": Text("else if () {") + Key("enter") + Text("}")
        + Key("up, end, left:3"),
        "else": Text("else {}") + Key("left, enter, up, end, enter"),
        "while": Text("while ") + Key("lparen, rparen, space, lbrace, enter, rbrace, up, end, left:3"),
        "for": Text("for ") + Key("lparen, rparen, space, lbrace, enter, rbrace, up, end, left:3"),
        "for range <i> increment": Text("for (int i = 0; i < %(i)s; i++) {}")
        + Key("left, enter, up, end, enter"),
        "for range <i> decrement": Text("for (int i = %(i)s; 0 <= i; i--) {}")
        + Key("left, enter, up, end, enter"),
        "print": Text("System.out.println();") + Key("left:2"),
        "import": Text("import ;") + Key("left"),
        "import <package>": Key("escape, colon, 1, enter, O") + Text("import %(package)s;"),
        "print string": Text('System.out.println("");') + Key("left:3"),
        "return": Text("return ;") + Key("left"),
        "ekint <i>": Text(" = %(i)d;"),
        "eknegint <i>": Text(" = -%(i)d;"),
        "ekvar <text>": Function(equals_variable, extras = {"text"}),
        "integer": Text("int"),
        "float": Text("float"),
        "double": Text("double"),
        "character": Text("char"),
        "new": Text("new "),
        "true": Text("true"),
        "false": Text("false"),
    }
    extras = [
        Choice("package", common_packages),        
        Integer("i", 0, 10000),
        Dictation("text"),
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

def define_class(text):
    """ Defins a class with name 'text' """
    Text("public class %s "%(format.pascal_case(text))).execute()
    Key("lbrace, rbrace, left, enter, up, end").execute()

def define_public_function(data_type, text):
    Text("public %s %s() {"
            %(data_type, format.snake_case(text))).execute()
    Key("enter, rbrace, up, end, left:3").execute()

def define_private_function(data_type, text):
    Text("private %s %s() {"
            %(data_type, format.snake_case(text))).execute()
    Key("enter, rbrace, up, end, left:3").execute()

def define_main_function():
    Text("public static void main(String[] args) {").execute()
    Key("enter, rbrace, up, end, enter").execute()


def declare_object_with_type(object_type, wrapper):
    Text(object_type).execute()
    # go inside <>
    Key("left").execute()
    Text(wrapper).execute()
    # move right and space
    # TODO: data_type is incorrect, needs to be replace with wrappers!
    Key("right, space").execute()

class VariablesRule(MappingRule):

    wrappers = {
            "integer": "Integer",
            "short": "Short",
            "float": "Float",
            "character": "Character",
            "double": "Double",
            "long": "Long",
            "boolean": "Boolean",
            }

    data_types = {
            "integer": "int",
            "short": "short",
            "float": "float",
            "character": "char",
            "double": "double",
            "void": "void",
            "long": "long",
            "boolean": "boolean",
    }

    object_types = {
            "array list": Text("ArrayList<>"),
            }

    mapping = {
            "define class <text>": Function(define_class, extra = {"text"}),
            "declare <text> as <data_type>": Function(declare_variable, extra = {"data_type", "text"}),
            "defunc main": Function(define_main_function),
            "defunc public <text> return <data_type>": Function(define_public_function, extra = {"data_type", "text"}),
            "defunc private <text> return <data_type>": Function(define_private_function, extra = {"data_type, text"}),
            "type <data_type>": Text("%(data_type)s"),
            "cast <data_type>": Text("(%(data_type)s)"),
            # Declaring objects
            "declare <object_type> type <wrapper>": Function(declare_object_with_type, extra = {"object_type", "wrapper"}),
    }
    extras = [
            Choice("wrapper", data_types),
            Choice("object_type", object_types),
            Choice("data_type", data_types),
            Dictation("text"),
            Integer("n", 1, 10),
    ]
    defaults = {
            "n": 5,        
    }

# Load and disable grammar
grammar = Grammar("java")
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
