from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()
