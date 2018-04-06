from .node import Node


class Queue:
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._size = 0

        if not isinstance(iter, (list, dict, tuple)):
            ''' check for iterable'''
            raise TypeError('It is not iterable.')
        for i in iter:
            self.enqueue(i)

    def enqueue(self, val):
        ''' add a value, increase size by 1'''
        node = Node(val)
        if self._size == 0:
            self.front = self.back = node
            self._size += 1
            return node
        # self.back.next = self.back = node
        self.back.next = node
        self.back = node
        self._size += 1
        return node

    def dequeue(self):
        ''' remove node from the front of queue'''
        if self._size == 0:
            raise IndexError

        temp = self.front
        self.front = temp._next
        self._size -= 1
        return temp
