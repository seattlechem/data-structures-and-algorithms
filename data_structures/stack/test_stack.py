from .stack import Stack
import pytest


def test_push(empty_stack):
    """ test for push val to empty stack """
    assert empty_stack.top is None
    empty_stack.push(23)
    assert empty_stack.top.val == 23
    assert empty_stack._size == 1


def test_typeerror_empty_stack():
    """ test for TypeError when you try to make an \
    instance of non-iterable argument."""
    with pytest.raises(TypeError):
        Stack(34-32)


def test_peek(small_stack):
    """ test for peek """
    assert small_stack.peek().val == 5


def test_empty_peek():
    """ test for peek on empty stack"""
    with pytest.raises(IndexError):
        empty = Stack()
        empty.peek()


def test_pop(small_stack):
    """ test for pop """
    assert small_stack.pop().val == 5


def test_empty_pop():
    """ test for pop on empty stack"""
    with pytest.raises(IndexError):
        empty = Stack()
        empty.pop()
