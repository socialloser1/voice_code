"""Module py_lang

This module contains general formatting for the Python language.

Author: Simon Larsen
version: 2016-08-28

"""
import format

# NOTE: Some words, like 'and' and 'or' do not result in Python syntax,
# general_programming is mainly aimed at C languages!
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
    Choice,
)

""" Creates an empty doc string

As of right now, this function is not working properly!
"""
def doc_string():
    Key("dquote:6, left:3").execute()

""" Function that prints out a Python function definition,
with the parameter text as the function name.
"""
def def_function(text):
    Text("def " + format.snake_case(str(text))).execute()

    # symbols added separately
    Key("lparen, rparen, colon, left:2").execute()

""" Outputs a class definition with the parameter
text as the class name.
"""
def def_class(text):
    Text("class " + format.pascal_case(str(text))).execute()
    Key("lparen, rparen, colon, left:2").execute()

""" Outputs 'text' = 'i', where multiple words in 'text' are snake-cased."""
def assign_int(text, i):
    Text(format.snake_case(str(text))  + " = " + str(i)).execute()

""" Outputs a for-each loop with the input parameter as the collection
to iterate over. If the parameter consists of several words, it will be snake-cased 
"""
def for_each(text):
    coll = format.snake_case(str(text))
    Text("for current in %s:"%(coll)).execute()
    Key("enter").execute()

""" The MappingRule for this module."""
class KeywordsRule( MappingRule ):
        # dict of mapping to keywords that require no special characters
        keywords = {
                "global": "global ",
                "true": "True",
                "false": "False",
                "break": "break",
                }
        
        # dict of common packages
        packages = {
                "system": "sys",
                "socket": "socket",
                "threading": "threading",
                }

	mapping = { 

        # Keywords
        "for": Text("for"),
        "else": Text("else") + Key("colon, enter"),
        "if": Text("if ") + Key("colon, left"),
        "elif": Text("elif ") + Key("colon, left"),
        "import": Text("import "),
        "import <package>": Text("import %(package)s") + Key("enter"),
        "while": Text("while ") + Key("colon, left"),
        "for": Text("for ") + Key("colon, left"),
        "length": Text("len") + Key("lparen, rparen, left"),
        "print": Text("print") + Key("lparen, rparen, left"),
        "print string": Text("print") + Key("lparen, dquote:2, rparen, left:2"),
        "<keyword>": Text("%(keyword)s"),
        "try": Text("try ") + Key("colon, left"),
        "except": Text("except ") + Key("colon, left"),
	}
	extras = [
                Dictation("text"),
                Integer("i", 0, 10000),
                Choice("keyword", keywords),
                Choice("package", packages),
	]
	defaults = {
                "i": 0,
    }

class VariablesRule(MappingRule):
    # python types
    data_types = {
            "integer": "int",
            "float": "float",
            "long": "long",
            "complex": "complex",
            "string": "str",
            "unicode": "unicode",
            "list": "list",
            "tuple": "tuple",
            "byte array": "bytearray",
            "buffer": "buffer",
            "ex range": "xrange",
            }


    mapping = {
        "[use] defunc <text>": Function(def_function, extra = {"text"}),
        "[use] pydoc": Function(doc_string),
        "[use] class <text>": Function(def_class, extra = {"text"}),
        "[use] assign <text> integer [<i>]": Function(assign_int, extra={"text", "i"}),
        "[use] for range [<i>]": Text("for i in range(%(i)d):"),
        "[use] for each <text>": Function(for_each, extra = {"text"}),
	"doc string": Function(doc_string),
        "cast <data_type>": Text("%(data_type)s") + Key("lparen, rparen, left"),
        }
    extras = [
            Dictation("text"),
            Integer("i", 0, 10000),
            Choice("data_type", data_types),
    ]
    defaults = {
            "i": 0,
    }

# Load and disable grammar
grammar = Grammar('python')
grammar.add_rule(KeywordsRule())
grammar.add_rule(VariablesRule())
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
