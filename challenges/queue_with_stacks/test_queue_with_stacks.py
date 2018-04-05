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
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_small_queue_size(small_queue):
    """ test size of Queue instance after 100 enqueue()"""
    assert small_queue._size == 100


def test_small_queue_dequeue(small_queue):
    '''
    small_queue is an instance of Queue object. Values from 0 to 99 were
    enqueued into stack1 of this instance in order.
    This tests if the order of values enqueued is preserved even after
    invoking dequeue method for 2 times consecutively, followed by
    enqueue, and finally dequeue. The expected value of node from the last
    dequeue is confirmed from this test.
    '''
    small_queue.dequeue()
    small_queue.dequeue()
    small_queue.enqueue(122)
    output = small_queue.dequeue()
    assert output.val == 2


def test_empty_queue_enqueue_dequeue(empty_queue):
    '''
    This test demonstrates the first value stored on an instance of this class
    will be extracted out first.
    '''
    empty_queue.enqueue('a')
    empty_queue.enqueue(43)
    empty_queue.enqueue('b')
    output = empty_queue.dequeue()
    assert output.val == 'a'


def test_small_queue_stack1_front(small_queue):
    '''
    This test confirms that values are enqueued into stack1 as first in first out.
    After inserting values from 0 to 99 consecutively, the stack1.top value is confirmed
    as the last enqueued value.
    '''
    assert small_queue.stack1.top.val == 99
