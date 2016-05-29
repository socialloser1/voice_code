# Interfaces the global commands ( Right now, only formatting ) with DNS via dragonfly

""" This module interfaces the global commands ( right now, only formatting ) With DNS via dragonfly.

Author: Simon Larsen
Version: 2016-05-26
"""

from dragonfly import ( Key, Function, Grammar,
                        Dictation, MappingRule, Text )

import format

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

class MainRule( MappingRule ):

	mapping = { 
        "[use] snay cass <text>": Function( snake_case_format, extra = {"text"} ),
        "[use] cam cass <text>": Function( camel_case_format, extra = {"text"} ),
        "[use] pass cass <text>": Function( pascal_case_format, extra = {"text"} ),
        "[use] cocol <text>": Function( concatenated_lower, extra = {"text"} ),
        "[use] cocup <text>": Function( concatenated_upper, extra = {"text"} ),
        "[use] low cass <text>": Function( lowercase, extra = {"text"} ),
        "[use] hi cass <text>": Function( uppercase, extra = {"text"} ),
	}
	extras = [
                Dictation( "text" ),
	]

grammar = Grammar('global')
grammar.add_rule(MainRule())
grammar.load()