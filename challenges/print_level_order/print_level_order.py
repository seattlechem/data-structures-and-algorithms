"""Print Level Order."""
from .k_tree import KTree as KT
from .queue import Queue


def print_order_level(input_kt=None):
    """Print out level-order node values."""
    if not type(input_kt) is KT:
        raise TypeError('Input must be K-ary Tree.')

    if input_kt is None:
        raise ValueError('Input is missing.')

    queue = Queue()
        queue.enqueue(self.root)
        while queue._length > 0:
            current = queue.dequeue()
            print(current.val + )
            for child in current.children:
                queue.enqueue(child)
