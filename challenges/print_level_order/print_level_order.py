"""Print Level Order."""
from .k_tree import KTree as KT
from .queue import Queue


def print_level_order(input_kt=None):
    """Print out level-order node values."""
    if input_kt is None:
        raise ValueError('Input is missing.')

    if not type(input_kt) is KT:
        raise TypeError('Input must be K-ary Tree.')

    queue = Queue()
    queue.enqueue(input_kt.root)
    result = ''

    while queue._length > 0:
        current = queue.dequeue()

        result += '{} '.format(current.val)

        if queue._length == 0:
            result += '\n'
            for child in current.children:
                queue.enqueue(child)

    return result
