from .node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0

        if not isinstance(iterable, (list, dict, tuple)):
            ''' check if iterable'''
            raise TypeError('It is not iterable.')   
        for i in iterable:
            self.push(i)

    def push(self, val):
        ''' Add a node'''
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('None value cannot be added.')

        node._next = self.top
        self.top = node
        self._size += 1

        return self.top

    def pop(self):
        ''' Remove node at the top. Decrease size by 1 and return val'''
        val = self.top
        self.top = self.top._next
        self._size -= 1
        return val

    def peek(self):
        ''' Look at the val at the top'''
        return self.top
