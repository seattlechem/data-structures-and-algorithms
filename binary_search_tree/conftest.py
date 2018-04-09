import pytest
from .bst import BST


@pytest.fixture
def eleven_element_bst():
    return BST([7, 1, 9, 0, 3, 8, 10, 2, 5, 4, 6])


@pytest.fixture
def empty_bst():
    return BST()
