"""Tree instersection test."""

from .tree_intersection import tree_intercept
import pytest


def test_return_true(bst1, bst2):
    """Confirm true."""
    result = tree_intercept(bst1, bst2)
    assert result == [0, 1, 2, 4, 5, 7, 9]


def test_nonbst_input():
    """Non BST type input."""
    with pytest.raises(TypeError):
        tree_intercept(12, 34)


def test_empty_bst(bst1, empty_bst):
    """Confirm nothing intercept with empty bst."""
    result = tree_intercept(bst1, empty_bst)
    assert result == []
