from .node import Node
from pythonds.basic.stack import Stack


class Queue:
    def __init__(self):
        self._size = 0
        self.stack1 = Stack()
        self.out_stack = Stack()

    def enqueue(self, val=0):
        """push value to stack1 """
        node = Node(val)

        self.stack1.push(node)

    def dequeue(self):
        """ extract the first value out """

        while len(self.stack1) != 0:
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()
