import pytest
from .find_maximum_value_binary_tree import find_maximum_value
from .bst import BST


def test_typeerror_true():
    """ test on input type """
    with pytest.raises(TypeError):
        find_maximum_value([1, 2, 3])


def test_maximum_five(five_element_bst):
    """ test for finding max from bst with five nodes. """
    b = find_maximum_value(five_element_bst)
    assert b == 9


def test_maximum_seven(seven_element_bst):
    """ test for finding max from bst with seven nodes. """
    b = find_maximum_value(seven_element_bst)
    assert b == 30


def test_empty():
    """ test for empty BST input """
    with pytest.raises(ValueError):
        find_maximum_value(BST())
