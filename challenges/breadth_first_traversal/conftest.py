from .bst import BST
import pytest


@pytest.fixture
def five_element_bst():
    """ creating five element bst """
    return BST([5, 1, 9, 0, 3])


@pytest.fixture
def seven_element_bst():
    """ creating seven element bst """ 
    return BST([15, 10, 12, 23, 9, 0, 30])
