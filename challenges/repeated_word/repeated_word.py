"""Repeated word whiteboard challenge."""

from .hash_table import HashTable as HH


def repeated_word(string_input):
    """Return the first word repeated more than once."""
    ss = string_input.split(" ")
    hh = HH()
    i = 0
    while len(ss) > 0:
        if hh.get(ss[i]):
            return ss
        hh.set(ss, 1)
        i += 1
