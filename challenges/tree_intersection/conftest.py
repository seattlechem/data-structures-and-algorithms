import pytest
from .bst import BST


@pytest.fixture
def bst1():
    return BST([7, 1, 9, 0, 3, 8, 10, 2, 5, 4, 6])


@pytest.fixture
def bst2():
    return BST([7, 1, 9, 0, 2, 4, 5, 2, 5, 5, 5])


@pytest.fixture
def bst3():
    return BST([15, 22, 25, 29, 30, 0, 7])


@pytest.fixture
def empty_bst():
    return BST()
