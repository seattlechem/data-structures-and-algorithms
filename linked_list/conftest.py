import pytest
from linked_list import LinkedList as ll
from node import Node


@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def small_ll():
    return ll([1, 2, 3, 4])


@pytest.fixture
def test_node():
    return Node(3, 4)
