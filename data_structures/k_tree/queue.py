class Node:
    """class called Node """
    def __init__(self, val, next=None):
        self.val = val
        self._next = next

    def __str__(self):
        return '{val}'.format(val=self.val)


class Queue:
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._length = 0

        if not isinstance(iter, (list, dict, tuple)):
            """ check for iterable """
            raise TypeError('It is not iterable.')
        for i in iter:
            self.enqueue(i)

    def enqueue(self, val):
        """ add a value, increase size by 1"""
        node = Node(val)

        if self._length == 0:
            self.front = self.back = node
            self._length += 1
            return node
        self.back._next = node
        self.back = node
        self._length += 1
        return node

    def dequeue(self):
        """ remove node from the front of queue """
        if self._length == 0:
            raise IndexError('You cannot dequeue() when front is empty')

        temp = self.front
        self.front = temp._next
        self._length -= 1
        return temp.val
