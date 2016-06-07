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

def equals_variable(text):
    Text("= %s"%(format.snake_case(text))).execute()

class OperationsRule(MappingRule):
    """ General operations, such as assignments """
    mapping = {
        "assign <text>": Function(assignment, extra = {"text"}),
        "call <text>": Function(function_call, extra = {"text"}),
        "ekint <n>": Text(" = %(n)d"),
        "eknegint <n>": Text(" = -%(n)d"),
        "ekvar <text>": Function(equals_variable, extra = {"text"}),
    }
    extras = [
        Dictation("text"),
        Integer("n", 0, 10000),
    ]

class SymbolsRule(MappingRule):
    """ Math and programming symbols, as well as indentation """
    mapping = {
        "Leta": Text(" < "),
        "Greta": Text(" > "),
        "Legreta": Text(" <>") + Key("left"),
        "Pew": Text(" + "),
        "Pec": Text(" += "),
        "Nay": Text(" - "),
        "Nayc": Text(" -= "),
        "Ek": Text(" = "),
        "Not ek": Text(" != "),
        "Ekek": Text(" == "),
        "Lek": Text(" <= "),
        "Gek": Text(" >= "),
        "Krax": Key("lbrace, rbrace, left"),
        "Brax": Key("lbracket, rbracket, left"),
        "Prain": Key("lparen, rparen, left"),
        "Duotes": Key("dquote, dquote, left"),
        "Indent [<n>]": Key("tab:%(n)d"),
    }
    extras = [
        Integer("n", 1, 8),    
    ]
    defaults = {
        "n": 1,        
    }

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
    """ Only for enabling and disabling other rules in this grammar.
    Note that the rules MUST be added in the 'rules' dict below for them to
    be activated by the 'general programming enable'-command !!! """
    rules = {
        "keywords": KeywordsRule(),
        "operations": OperationsRule(),
        "symbols": SymbolsRule(),
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
