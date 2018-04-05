# from .node import Node
from .stack import Stack


class Queue:
    def __init__(self):
        self._size = 0
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val=0):
        """push value to stack1 """
        self.stack1.push(val)
        self._size += 1

    def dequeue(self):
        """ extract the first value out """
        # if self._size == 0:
        #     raise TypeError('Cannot dequeue the empty queue object')

        while self.stack1._size != 0:
            self.stack2.push(self.stack1.pop())
        output = self.stack2.pop()

        if self.stack2._size != 0:
            self.stack1.push(self.stack2.pop())

        return output
