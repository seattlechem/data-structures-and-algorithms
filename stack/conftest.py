from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    return Stack([1, 2, 3, 4, 5])

