"""Correct spellings"""

from os import path

import hunspell
from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Spell"
__version__ = "0.1"
__trigger__ = "spell "
__author__ = "Bharat Kalluri"
__dependencies__ = ['hunspell']

icon_path = "{}/icons/{}.png".format(path.dirname(__file__), "correction")


def handleQuery(query):
    if query.isTriggered:
        if not query.isValid:
            return

        if query.string.strip():
            return parse_input(query.string)
        else:
            return Item(
                id=__prettyname__,
                icon=icon_path,
                text=__prettyname__,
                subtext="Type in a spelling to see the correct spelling",
                completion=query.rawString,
            )


def parse_input(word):
    spellchecker = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
    response = spellchecker.suggest(word)
    results = []
    if len(response) > 0:
        for replacements in response:
            results.append(Item(
                id=__prettyname__,
                icon=icon_path,
                text=replacements,
                subtext='',
                actions=[ClipAction("Copy to clipboard", str(replacements))]
            ))
    return results
