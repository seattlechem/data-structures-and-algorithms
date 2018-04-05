import pytest
from .queue_with_stacks import Queue
from .node import Node
from .stack import Stack


@pytest.fixture
def empty_queue():
    return Queue()
