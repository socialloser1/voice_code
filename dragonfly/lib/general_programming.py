""" Module that ocntains voice macros for common formatting
found in most object oriented programming. Mainly consists of
keywords such as 'if', 'and' etc.

This module is fully compatible for use in VIM in Bash on Windows.
It is partially compatible with other text editors like Sublime Text.
Some commands may behave unexpededly in the latter.

Author: Simon Larsen
Version: 2016-06-15
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
    call = "." + format.snake_case(text)
    Text(call).execute()
    # Place cursor inside parens
    Key("lparen, rparen, left").execute()

def equals_variable(text):
    Text(" = %s"%(format.snake_case(text))).execute()

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
        "Insert new line": Key("backslash, n"),
        "Sqrt": Text("sqrt") + Key("lparen, rparen, left"),
        "Leta": Key("space, langle, space"),
        "Greta": Key("space, rangle, space"),
        "Legreta": Key("space, langle, rangle, left"),
        "Multi": Key("space, asterisk, space"),
        "Multek": Key("space, asterisk, equal, space"),
        "Div": Key("space, slash, space"),
        "Divek": Key("space, slash, equal, space"),
        "Mod": Key("space, percent, space"),
        "Not": Key("exclamation"),
        "Pew": Key("space, plus, space"),
        "Increment": Key("plus, plus"),
        "Pec": Key("space, plus, equal, space"),
        "Nay": Key("space, minus, space"),
        "Decrement": Key("minus, minus"),
        "Nayc": Key("space, minus, equal, space"),
        "Ek": Key("space, equal, space"),
        "Not ek": Key("space, exclamation, equal, space"),
        "Ekek": Key("space, equal:2, space"),
        "Lek": Key("space, langle, equal, space"),
        "Gek": Key("space, rangle, equal, space"),
        "Doll": Key("dollar"),
        "Krax": Key("lbrace, rbrace, left"),
        "Brax": Key("lbracket, rbracket, left"),
        "Prain": Key("lparen, rparen, left"),
        "Duotes": Key("dquote, dquote, left"),
        "squotes": Key("squote, squote, left"),
        "Indent [<n>]": Key("tab:%(n)d"),
        "Hash": Key("hash"),
        "Perk": Key("percent"),
        "U score": Key("underscore"),
        "Amp": Key("ampersand"),
        "Star": Text("*"),
        "Bang": Key("exclamation"),
        "Or": Key("space, bar:2, space"),
        "Bitwise or": Key("space, bar, space"),
        "And": Key("space, ampersand:2, space"),
        "Bitwise and": Key("space, ampersand, space"),
        "Ex or": Key("space, caret, space"),
        "Bitwise left": Key("langle:2"),
        "Bitwise right": Key("rangle:2"),
        # python 'and' and 'or'
        "Pand": Text(" and "),
        "Poor": Text(" or "),
        # c style comment and block comment
        "See comment": Key("slash:2, space"),
        "See block comment": Key("slash, asterisk:2, enter:2, slash, up, space"),
    }
    extras = [
        Integer("n", 1, 8),    
    ]
    defaults = {
        "n": 1,        
    }

class KeywordsRule(MappingRule):
    mapping = {
        "<text>": Text("%(text)s"), # this line makes sure there's no annoying start space
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
