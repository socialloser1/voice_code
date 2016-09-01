""" Module vim

This module contains vim commands.

Author: Simon Larsen
Version: 2016-06-15

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

def insertion(insert, line = -1):
    command_mode()

    if 0 < line:
        go_to_line(line)

    Key(insert).execute()

def command_mode():
    Key("escape").execute()

def set_command(command_choice):
    execute_command("set " + command_choice)

def execute_command(command, force = False):
    enter_command(command, force)
    Key("enter").execute()

def enter_command(command, force = False):
    command_mode()
    command.execute()
    if force:
        Text("!").execute()

def go_to_line(line):
    execute_command(Text(":%s"%(line)))

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
            "write": Text(":w"),
            "quit": Text(":q"),
            "write and quit": Text(":wq"),
            "search and replace": Text(":%s///gc") + Key("left:4"),
            "search and replace precise": Text(":%s/\<\>//gc") + Key("left:6"),
            "search precise": Text("/\<\>") + Key("left:2"),
            "clear search": Key("c-l"),
    }

    mapping = {
        "[use] insert [<insert>]": Function(insertion, extra = {"insert"}),
        "[use] insert [<insert>] line <line>": Function(insertion, extra={"insert", "line"}),
        "[enable] command mode":  Function(command_mode),
        "[go to] line <line>": Function(go_to_line, extra = {"line"}),
        "[use] undo": Function(command_mode) + Key("u"),
        "[use] redo": Function(command_mode) + Key("c-R"),
        "[use] redraw": Function(command_mode) + Key("c-l"),
        "[use] delete line": Function(command_mode) + Key("d, d"),
        "[use] delete line <line>": Function(go_to_line, extra = {"line"}) + Key("d, d"),
        "yes": Text("Y"),
        "no": Text("N"),
        "command <command>": Function(enter_command, extra = {"command"}),
        "execute command <command>": Function(execute_command, extra = {"command"}),
        "force command <command>": Function(enter_command, extra = {"command"}, force = True),
        "force execute command <command>": Function(execute_command, extra = {"command"}, force = True),
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
