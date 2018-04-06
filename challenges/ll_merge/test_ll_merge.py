# import pytest
from .linked_list import LinkedList
from .ll_merge import merge_lists
# from .node import Node


def test_simple_merge_true():
    ll1 = LinkedList([1, 3, 5])
    ll2 = LinkedList([2, 4, 6])

    head = merge_lists(ll1, ll2)
    assert head.val == 1
