"""Fixtures."""

import pytest
from .bst import BST


@pytest.fixture
def bst1():
    """Eleven member bst."""
    return BST([7, 1, 9, 0, 3, 8, 10, 2, 5, 4, 6])


@pytest.fixture
def bst2():
    """Another Eleven member bst."""
    return BST([7, 1, 9, 0, 2, 4, 5, 2, 5, 5, 5])


@pytest.fixture
def bst3():
    """Seven member bst."""
    return BST([15, 22, 25, 29, 30, 0, 7])


@pytest.fixture
def empty_bst():
    """Empty bst."""
    return BST()
