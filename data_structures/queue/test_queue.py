import pytest


def test_enqueue(empty_queue):
    """ test when you add value to empty queue"""
    assert empty_queue.front is None
    assert empty_queue.back is None
    empty_queue.enqueue(23)
    assert empty_queue.front.val == 23


def test_empty_argument_enqueue(empty_queue):
    """
    test to see if TypeError is raised when invoke
    enqueue with no argument
    """
    with pytest.raises(TypeError):
        empty_queue.enqueue()


def test_dequeue(small_queue):
    """ test the value of front node when dequeue is invoked """
    assert small_queue.dequeue().val == 1


def test_index_error_dequeue(empty_queue):
    """
    test to see if index error raises when trying to \
    dequeue the empty queue
    """
    with pytest.raises(IndexError):
        empty_queue.dequeue()
