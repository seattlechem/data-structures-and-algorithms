import pytest
from .linked_list import LinkedList as ll


def test_insert_first_node(empty_ll):
    """test for insert node"""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2
    empty_ll.insert(5)
    assert empty_ll.head.val == 5


def test_insert_empty_list(small_ll):
    ''' test for insert empty list'''
    small_ll.insert([])
    assert small_ll.head.val == []


def test_instantiate_non_iterable():
    ''' test for type error occurred when
    intantiate with non-literable '''
    with pytest.raises(TypeError):
        ll(3)


def test_find(small_ll):
    """test for find method"""
    assert small_ll.find(2) is True


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


def test_append(small_ll):
    ''' test for append'''
    small_ll.append(5)
    assert str(small_ll) == '[1, 2, 3, 4, 5]'


def test_insert_before(small_ll):
    ''' test for insert_before''' 
    small_ll.insert_before(2, 10)
    assert str(small_ll) == '[1, 10, 2, 3, 4]'


def test_insert_before_value_error(small_ll):
    ''' test for insert_before value error
    when trying to add value at out of
    index point
    ''' 
    with pytest.raises(ValueError):
        small_ll.insert_before(5, 10)


def test_insert_after(small_ll):
    ''' test for insert_after'''
    small_ll.insert_after(2, 10)
    assert str(small_ll) == '[1, 2, 10, 3, 4]'


def test_insert_after_value_error(small_ll):
    ''' test for insert_after value error
    when trying to add value at out of
    index point
    ''' 
    with pytest.raises(ValueError):
        small_ll.insert_before(5, 10)


def test_type_error_with_linked_list():
    ''' test for linked_list when trying to
    instantiate with uniterate value
    ''' 
    with pytest.raises(TypeError):
        ll(10)
