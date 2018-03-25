from node import Node


class LinkedList:
    """class called LinkedList """
    def __init__(self):
        self.head = None
   
    def insert(self, newNode):
        if self.head is None:
            self.head - newNode

linkedlist = LinkedList()
# when linked list is initialized, head is none
