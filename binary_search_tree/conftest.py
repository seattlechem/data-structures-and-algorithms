import pytest
from .bst import BST


@pytest.fixture
def eleven_element_bst():
    return BST([7, 1, 9, 0, 3, 8, 10, 2, 5, 4, 6])


@pytest.fixture
def five_element_bst():
    return BST([5, 1, 9, 0, 3])


@pytest.fixture
def seven_element_bst():
    return BST([15, 10, 12, 23, 9, 0, 30])


@pytest.fixture
def empty_bst():
    return BST()
