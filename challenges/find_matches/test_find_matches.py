"""Test cases."""

from .k_tree import KTree
from .linked_list import LinkedList
from .k_tree import Node
from .find_matches import find_matches
import pytest


def test_small_tree_find_five(small_tree):
    """Check if find_match function find all nodes with value 5."""
    ls = list()
    result = find_matches(small_tree, 5)
    # import pdb; pdb.set_trace()
    assert isinstance(result, list) is True
    for _ in range(0, 3):
        ls.append(Node(5))
    # import pdb; pdb.set_trace()
    assert result == ls
