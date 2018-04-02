from .stack import Stack
import pytest


def test_push(empty_stack):
    ''' test for push val to empty stack'''
    assert empty_stack.top is None
    assert empty_stack.push(23).val == 23
    assert empty_stack._size == 1
