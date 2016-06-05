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
    Text,
    Choice
)

def select_all(unit_type):
    Key("c-%s"%(unit_type)).execute()
    
class MainRule(MappingRule):
    unit_types = {
    "cavalry": "c",
    "infantry": "i",
    "missile": "m",
    }
    mapping = {
    "group up": Key("g"),
    "[select] group <i>": Key("i"),
    "lock [group]": Key("c-g"),
    "[Select] all <unit_type>": Function(select_all, extra = {"unit_type"}),
    "Select all simple <unit_type>": Key("c-%(unit_type)s"),
    }
    extras = [
        Integer("i", 1, 9),
        Choice("unit_type", unit_types),
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
