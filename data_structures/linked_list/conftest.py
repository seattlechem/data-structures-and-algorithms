import pytest
from .linked_list import LinkedList as ll
from .node import Node


@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def small_ll():
    return ll([1, 2, 3, 4])


@pytest.fixture
def test_node():
    return Node(3, 4)


@pytest.fixture
def small_linked_list_with_loop():
    small_ll = ll([1, 2, 3, 4, 5])
    current = small_ll.head
    temp = current._next
    while current._next:
        current = current._next
    current._next = temp
    return small_ll


@pytest.fixture
def big_linked_list_with_loop():
    ls = []
    for i in range(0, 100):
        ls.append(i)
    big_linked_list = ll(ls)

    current = big_linked_list.head
    temp = current._next
    while current._next:
        current = current._next
    current._next = temp
    return big_linked_list


@pytest.fixture
def long_linked_list():
    ls = []
    for i in range(0, 1000):
        ls.append(i)
    long_linked_list = ll(ls)
    return long_linked_list
