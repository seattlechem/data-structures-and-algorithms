import pytest


def test_empty_queue_size(empty_queue):
    '''
    test to see if dequeue on an instance of
    Queue object which has only one value
    returns the expected value.
    '''
    empty_queue.enqueue(3)
    output = empty_queue.dequeue()
    assert output.val == 3


def test_dequeue_on_empty_queue(empty_queue):
    '''
    test to see if dequeue on an instance of empty
    Queue object raises error
    '''
    with pytest.raises(TypeError):
        empty_queue.dequeue()
