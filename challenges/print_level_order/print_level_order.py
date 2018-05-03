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

    queue = Queue()
    queue.enqueue(input_kt.root)
    result = ''

    counter = 1
    import pdb; pdb.set_trace()
    while queue._length > 0:
        current = queue.dequeue()
        counter -= 1

        result += '{} '.format(current.val)
        # print('value:', current.val)
        if counter == 0:
            result += '\n'

        for child in current.children:
            # print('value:', child.val)
            queue.enqueue(child)
            counter += 1

    return result
