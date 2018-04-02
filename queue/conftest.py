from .queue import queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    return Queue([1, 2, 3, 4, 5])
