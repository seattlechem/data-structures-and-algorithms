"""Print Level Order."""
from .k_tree import KTree as KT
from .queue import Queue
from .k_tree import Node


def print_level_order(input_kt=None):
    """Print out level-order node values."""
    if input_kt is None:
        raise ValueError('Input is missing.')

    if not type(input_kt) is KT:
        raise TypeError('Input must be K-ary Tree.')

    queue1 = Queue()
    queue2 = Queue()
    result = ''

    queue1.enqueue(input_kt.root)

    while queue1._length > 0:
        current = queue1.dequeue()

        result += f'{current.val} '

        for child in current.children:
            queue2.enqueue(child)

        if queue1._length == 0:
            queue1, queue2 = queue2, queue1
            result += '\n '

    return result
