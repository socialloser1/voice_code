# Interfaces the global commands ( Right now, only formatting ) with DNS via dragonfly

""" This module interfaces the global commands ( right now, only formatting ) With DNS via dragonfly.

Author: Simon Larsen
Version: 2016-05-26
"""

from dragonfly import ( Key, Function, Grammar,
                        Dictation, MappingRule, Text, Choice )

from lib import (format, python, c_lang, vim)

# Functions that execute different kinds of formatting on text
def snake_case_format(text):
	Text( format.snake_case( str( text ) ) ).execute()

def camel_case_format( text ):
	Text( format.camel_case( str( text ) ) ).execute()

def pascal_case_format( text ):
	Text( format.pascal_case( str( text ) ) ).execute()

def concatenated_lower( text ):
	Text( format.no_space_lower( str( text ) ) ).execute()

def concatenated_upper( text ):
	Text( format.no_space_upper( str( text ) ) ).execute()

def lowercase( text ):
	Text(format.lowercase_letters(str(text))).execute()

def uppercase( text ):
	Text(format.uppercase_letters(str(text))).execute()

def enable_grammar(choice):
	choice.enable()

def disable_grammar(choice):
    choice.disable()

class MainRule( MappingRule ):
	""" This rule always loads when NatLinks starts, and is always enabled.
	Therefore, the mappings below are always available.

	The grammars in the grammar_modules dictionary can be enable/disabled by saying:
	'enable / disable grammar <name of module>'

	NOTE: There is as of yet NO compatability check between grammar modules, so beware
	when enabling / disabling them!
	"""
	grammar_modules = {
	    "python": python,
	    "vim": vim,
	}

	mapping = { 
        "[use] snake <text>": Function( snake_case_format, extra = {"text"} ),
        "[use] camel <text>": Function( camel_case_format, extra = {"text"} ),
        "[use] pascal <text>": Function( pascal_case_format, extra = {"text"} ),
        "[use] cocol <text>": Function( concatenated_lower, extra = {"text"} ),
        "[use] cocup <text>": Function( concatenated_upper, extra = {"text"} ),
        "[use] spell low <text>": Function( lowercase, extra = {"text"} ),
        "[use] spell high <text>": Function( uppercase, extra = {"text"} ),
        "[use] enable grammar <choice>": Function(enable_grammar, extra = {"choice"}),
        "[use] disable grammar <choice>" : Function(disable_grammar, extra = {"choice"}),
	}
	extras = [
                Dictation("text"),
                Choice("choice", grammar_modules),
	]

grammar = Grammar('global')
grammar.add_rule(MainRule())
grammar.load()
