""" Module vim

This module contains vim commands.

Author: Simon Larsen
Version: 2016-06-02

"""
import format

from dragonfly import (
    Function,
    MappingRule,
    Integer,
    Grammar,
    Dictation,
    Choice,
    Key,
    Text
)

command_mode = True

# Remember to set command_mode = False when insert/visual/select etc!
def insertion(insert):
    global command_mode
    if command_mode:
        Key(insert).execute()
        command_mode = False
    else:
        print ("Not in command mode!\n"
        + "If you opened a new Vim session, please issue the 'command mode' voice command.")

def enable_command_mode():
    global command_mode
    if not command_mode:
        Key("escape").execute()
        command_mode = True

class MainRule(MappingRule):
    # Different points of insertion
    insert_points = {
    "before": "i",
    "at home": "I",
    "after": "a",
    "at end": "A",
    "above": "O",
    "below": "o",
    }

    mapping = {
    "[use] insert [<insert>]": Function(insertion, extra = {"insert"}),
    "[enable] command mode":  Function(enable_command_mode),
    }
    extras = [
        Dictation("text"),
	Choice("insert", insert_points),
    ]
    defaults = {
    "insert": "i",
    }


# Load and disable grammar
grammar = Grammar("vim")
grammar.add_rule(MainRule())
grammar.load()
grammar.disable()

# Functions that enable and disable this grammar
def enable():
    global grammar
    if not grammar.enabled:
        grammar.enable()

def disable():
    global grammar
    if grammar.enabled:
        grammar.disable()
