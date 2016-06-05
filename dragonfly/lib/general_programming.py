""" Module that ocntains voice macros for common formatting
found in most object oriented programming. Mainly consists of
keywords such as 'if', 'and' etc.

Author: Simon Larsen
Version: 2016-06-03
"""
import format

from dragonfly import (
    Function,
    MappingRule,
    Integer,
    Dictation,
    Text,
    Key,
    Grammar,
    Choice
)

def assignment(text):
    # Assumes snake cased variables
    Text(format.snake_case(text) + " = ").execute()

def function_call(text):
    # Assumes snake cased functions
    call = "." + format.snake_case(text) + "()"
    Text(call).execute()
    # Place cursor inside parens
    Key("left").execute()



class OperationsRule(MappingRule):
    """ General operations, such as assignments """
    mapping = {
        "assign <text>": Function(assignment, extra = {"text"}),
        "call <text>": Function(function_call, extra = {"text"}),
    }
    extras = [
        Dictation("text"),        
    ]

class KeywordsRule(MappingRule):
    mapping = {
        "if": Text("if"),
        "while": Text("while"),
        "break": Text("break"),
        "for": Text("for"),
        "integer": Text("int"),
        "double": Text("double"),
        "float": Text("float"),
    }

def enable_rule(rule):
    global grammar
    if rule not in grammar.rules:
        grammar.unload()
        grammar.add_rule(rule)
        grammar.load()

def disable_rule(rule):
    global grammar
    if rule in grammar.rules:
        grammar.unload()
        grammar.remove_rule(rule)
        grammar.load()

class MainRule(MappingRule):
    """ Only for enabling and disabling other rules in this grammar """
    rules = {
        "keywords": KeywordsRule(),
        "operations": OperationsRule(),
    }

    mapping = {
        "general programming enable <rule>": Function(enable_rule, extra = {"rule"}),
        "general programming disable <rule>": Function(disable_rule, extra = {"rule"})
    }
    extras = [
        Choice("rule", rules),        
    ]

# Load and is able grammar
grammar = Grammar("programming")
grammar.add_rule(MainRule())
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
