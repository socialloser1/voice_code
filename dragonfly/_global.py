#Interfaces the global commands ( Right now, only formatting ) with DNS via dragonfly

""" This module interfaces the global commands ( right now, only formatting ) With DNS via dragonfly.

Author: Simon Larsen
Version: 2016-08-31
"""

from dragonfly import ( Key, Function, Grammar,
                        Dictation, MappingRule, Text, Choice, Integer )

from lib import (java, general_programming, format, python, c_lang, vim, markdown)

# Functions that execute different kinds of formatting on text
def format_text(text, format_function):
    output = format_function(text)
    Text(output).execute()

def enable_grammar(choice):
	choice.enable()

def disable_grammar(choice):
    choice.disable()

def print_date(day, month):
    Text(format.format_date(month, day)).execute()


class MainRule( MappingRule ):
    """ This rule always loads when NatLinks starts, and is always enabled.
    Therefore, the mappings below are always available.

    The grammars in the grammar_modules dictionary can be enable/disabled by saying:
    'enable / disable grammar <name of module>'

    NOTE: There is as of yet NO compatability check between grammar modules, so beware
    when enabling / disabling them!
    """
    functions = {
            "snake": "format.snake_case",
            "camel": "format.camel_case",
            }

    mapping = {
        "[use] snake <text>": Function(format_text, text = "%(text)s", format_function = format.snake_case),
        "[use] camel <text>": Function(format_text, text = "%(text)s", format_function = format.camel_case),
        "[use] pascal <text>": Function(format_text, text = "%(text)s", format_function = format.pascal_case),
        "[use] cocol <text>": Function(format_text, text = "%(text)s", format_function = format.no_space_lower),
        "[use] cocup <text>": Function(format_text, text = "%(text)s", format_function = format.no_space_upper),
        "[use] spell low <text>": Function(format_text, text = "%(text)s", format_function = format.lowercase_letters),
        "[use] spell high <text>": Function(format_text, text = "%(text)s", format_function = format.uppercase_letters),
        "[use] lowercase <text>": Text("%(text)s".lower()),
        "[use] uppercase <text>": Text("$(text)s".upper()),
        "[use] date <day> of <month>": Function(format.format_date, extra = {"month, day"})
    }
    extras = [
        Choice("function", functions),
        Dictation("text"),
        Choice("month", format.months),
        Integer("day", 1, 31),
    ]

class GrammarRule(MappingRule):
    """ This rule handles enabling and disabling of grammars """
    # Add new modules here to be able to enable/disable them with voice commands
    grammar_modules = {
        "python": python,
        "vim": vim,
        "general programming": general_programming,
        "see": c_lang,
        "java": java,
        "markdown": markdown,
    }

    def enabled_modules(self):
        for current in grammar_modules:
            if current.enabled:
                print current

    mapping = {
        "[use] enable grammar <choice>": Function(enable_grammar, extra = {"choice"}),
        "[use] list enabled modules": Function(enabled_modules),
        "[use] disable grammar <choice>" : Function(disable_grammar, extra = {"choice"}),
    }
    extras = [
        Choice("choice", grammar_modules),
    ]

def switch_desktop(direction):
    if direction == "left":
        Key("cw-left").execute()
    elif direction == "right":
        Key("cw-right").execute()
    else:
        print("Incorrect direction!")

class WindowsRule(MappingRule):
    """ This rule contains voice commands for manipulation windows and virtual desktops """
    directions = {
        "left": "left",
        "right": "right",
        "down": "down",
        "up": "up",
    }

    mapping = {
        "[switch] desktop <direction>": Function(switch_desktop, extra = {"direction"}),
        "[snap] window <direction>": Key("w-%(direction)s"),
    }
    extras = [
        Choice("direction", directions),
    ]

grammar = Grammar('global')
grammar.add_rule(MainRule())
grammar.add_rule(GrammarRule())
grammar.add_rule(WindowsRule())
grammar.load()
