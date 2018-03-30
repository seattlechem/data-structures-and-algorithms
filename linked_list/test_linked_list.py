import pytest


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
    """test for str representation for empty linked list"""
    assert str(empty_ll) == 'List is empty'


def test_str_node(test_node):
    """test for str representation of node"""
    assert str(test_node) == '3'
