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
def insertion(insert, line = -1):
    global command_mode
    if not command_mode:
        enable_commande_mode()

    if 0 < line:
        go_to_line(line)

    Key(insert).execute()
    command_mode = False

def enable_command_mode():
    global command_mode
    Key("escape").execute()
    command_mode = True

def set_command(command_choice):
    execute_command("set " + command_choice)

def execute_command(text):
    enable_command_mode()
    Text(":%s"%(text)).execute()
    Key("enter").execute()

def go_to_line(line):
    execute_command(str(line))

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

    commands = {
        "write": "w",
        "quit": "q",
        "write and quit": "wq",
    }

    mapping = {
        "[use] insert [<insert>]": Function(insertion, extra = {"insert"}),
        "[use] insert [<insert>] line <line>": Function(insertion, extra={"insert", "line"}),
        "[enable] command mode":  Function(enable_command_mode),
        "[go to] line <line>": Function(go_to_line, extra = {"line"}),
        "[use] undo": Function(enable_command_mode) + Key("u"),
        "[use] redo": Function(enable_command_mode) + Key("c-R"),
        "[use] write to file": Function(execute_command, text = "w"),
        "[use] quit": Function(execute_command, text = "q"),
        "command <command>": Function(execute_command, extras = {"command"}),
        "force command <command>": Function(execute_command, text = "%(command)s!"),
    }
    extras = [
        Dictation("text"),
	Choice("insert", insert_points),
        Choice("command", commands),
        Integer("line", 1, 10000),
    ]
    defaults = {
        "insert": "line",
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
