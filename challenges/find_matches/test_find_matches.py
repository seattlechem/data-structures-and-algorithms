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

    assert isinstance(result, list) is True

    ls.append(small_tree.root.children[0])
    ls.append(small_tree.root.children[0].children[0])
    ls.append(small_tree.root.children[3])

    assert result == ls


def test_small_tree_not_found(small_tree):
    """Check if code break when searching for value not found."""
    result = find_matches(small_tree, 2)
    assert result == []
