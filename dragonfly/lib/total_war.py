""" Module total_war

Contains voice macros for the Total War series.
This modules is mainly aimed at Warhammer total war,
but will probably work for other total wars as well.

Author:  Simon Larsen
Version:  2016-06-02
"""
import format
from dragonfly import (
    Function,
    MappingRule,
    Integer,
    Grammar,
    Dictation,
    Key,
    Text 
)

class MainRule(MappingRule):
    mapping = {
    "group up": Key("g"),
    "[select] group <i>": Key("i"),
    }
    extras = [
        Integer("i"),
    ]

# Load and is able grammar
grammar = Grammar("total war")
grammar.add_rule(MainRule())
grammar.load()
grammar.disable()

# Functions that enable and disable the grammar
def enable():
    global grammar
    if not grammar.enabled:
        grammar.enable()

def disable():
    global grammar
    if grammar.enabled:
        grammar.disable()
