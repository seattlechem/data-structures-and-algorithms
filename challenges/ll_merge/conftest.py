import pytest
from .linked_list import LinkedList


@pytest.fixture
def ll1():
    return LinkedList([1, 4, 7])


@pytest.fixture
def ll2():
    return LinkedList([2, 5, 8])


@pytest.fixture
def ll1_one():
    return LinkedList([1])


@pytest.fixture
def ll2_one():
    return LinkedList([2])
