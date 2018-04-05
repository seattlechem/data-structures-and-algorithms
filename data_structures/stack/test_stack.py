from .stack import Stack
import pytest


def test_push(empty_stack):
    """ test for push val to empty stack """
    assert empty_stack.top is None
    assert empty_stack.push(23).val == 23
    assert empty_stack._size == 1


def test_typeerror_empty_stack():
    with pytest.raises(TypeError):
        Stack(34-32)


def test_peek(small_stack):
    """ test for peek """
    assert small_stack.peek().val == 5


def test_pop(small_stack):
    """ test for pop """
    assert small_stack.pop().val == 5
