# Interfaces the global commands ( Right now, only formatting ) with DNS via dragonfly

''' This module interfaces the global commands ( right now, only formatting ) With DNS via dragonfly.

Author: Simon Larsen
Version: 2016-05-26
'''

from dragonfly import ( Key, Function, Grammar,
                        Dictation, MappingRule, Text )

import format

def snake_case_format( text ):
	Text( format.snake_case( text ) ).execute()

def camel_case_format( text ):
	Text( format.camel_case( text ) ).execute()

class MainRule( MappingRule ):

	mapping = { 
        "[use] snay cass [<text>]" : Function( snake_case_format, extra = {"text"} ),
        "[use] cam cass [<text>]" : Function( camel_case_format, extra = {"text"} ),
	}
	extras = [
                Dictation( "text" ),
	]
	defaults = {"text": "",
    }

grammar = Grammar('global')
grammar.add_rule(MainRule())
grammar.load()

