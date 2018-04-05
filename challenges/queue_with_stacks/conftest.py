import pytest
from .queue_with_stacks import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    small_queue = Queue()
    counter = 0
    while counter < 100:
        small_queue.enqueue(counter)
        counter += 1
    return small_queue
