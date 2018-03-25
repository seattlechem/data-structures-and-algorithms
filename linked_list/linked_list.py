from node import Node


class LinkedList:
    """class called LinkedList """
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode


# instantiate first node with data "john"
first_node = Node("john")
# instantiate linkedlist
linkedlist = LinkedList()
# 
