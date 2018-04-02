from .node import Node


class Queue:
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0

        if not isinstance(iter, (list, dict, tuple)):
            ''' check for iterable'''
            raise TypeError('It is not iterable.')  
        for i in iter:
            self.enqueue(i)

    def enqueue(self, val):
        ''' add a value, increase size by 1'''
        self.head = Node(val, self.head)
        self._size += 1

    def dequeue(self):
        ''' remove node from the front of queue'''
        node = self.head
        self.head = self.head._next
        self._size -= 1
        return node
