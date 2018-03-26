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
    return Node(3, 4, 5)


def test_insert_first_node(empty_ll):
    """test for insert node"""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_len(small_ll):
    """test len for LinkedList"""
    assert len(small_ll) == 4


def test_str(small_ll):
    """test str for linkedlist"""
    assert str(small_ll) == '[1, 2, 3, 4]'


def test_empty_str(empty_ll):
    assert str(empty_ll) == 'List is empty'
