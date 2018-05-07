"""Test fixtures."""

import pytest
from .hash_table import HashTable as HT


@pytest.fixture
def five_key_ht():
    """Create five element HT."""
    hashe_1 = HT()
    sample = {
        'color': 'red',
        'scent': 'apple',
        'favorite': 'skiing',
        'restaurant': 'izumi',
        'number': 13,
    }

    for key, val in sample.items():
        hashe_1.set(key, val)

    return hashe_1


@pytest.fixture
def six_key_ht():
    """Create five element HT."""
    hashe_2 = HT()
    sample = {
        'color': 'red',
        'scent': 'starwberry',
        'favorite': 'swimming',
        'restaurant': 'maneki',
        'number': 8,
        'cost': 0
    }

    for key, val in sample.items():
        hashe_2.set(key, val)

    return hashe_2
