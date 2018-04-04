from .queue import Queue
import pytest


def test_enqueue(empty_queue):
    ''' '''
    empty_queue.enqueue(23)
    assert empty_queue.head.val == 23
