import pytest
from linked_list import LinkedList as ll
from node import Node


@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def small_ll():
    return ll([1, 2, 3, 4])


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2
