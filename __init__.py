"""Correct spellings"""

from os import path

import hunspell
from albert import *

__title__ = "Spell"
__version__ = "0.4.0"
__triggers__ = "spell "
__authors__ = ["Bharat Kalluri", "Faris Redza"]
__py_deps__ = ["hunspell"]

iconPath = "{}/icons/{}.png".format(path.dirname(__file__), "correction")

def handleQuery(query):
    if query.isTriggered:
        if not query.isValid:
            return

        if query.string.strip():
            return parse_input(query.string)
        else:
            return Item(
                id=__title__,
                icon=iconPath,
                text=__title__,
                subtext="Type in a spelling to see the correct spelling",
                completion=query.rawString,
            )


def parse_input(word):
    spellchecker = hunspell.HunSpell('/usr/share/hunspell/en_GB.dic', '/usr/share/hunspell/en_GB.aff')
    response = spellchecker.suggest(word)
    results = []
    if len(response) > 0:
        for replacements in response:
            results.append(Item(
                id=__title__,
                icon=iconPath,
                text=replacements,
                subtext='',
                actions=[ClipAction("Copy to clipboard", str(replacements))]
            ))
    return results
