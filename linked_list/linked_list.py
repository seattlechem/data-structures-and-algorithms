from node import Node


class LinkedList:
    """class called LinkedList """
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node._next is None:
                    break
                last_node = last_node._next
            last_node._next = new_node


# instantiate first node with data "john"
first_node = Node("john")
# instantiate linkedlist
linkedlist = LinkedList()
# add first_node into linkedlist using insert method
linkedlist.insert(first_node)
# instantiate second_node and insert
second_node = Node('Ben')
linkedlist.insert(second_node)
# instantiate third_node and insert
third_node = Node('Matthew')
linkedlist.insert(third_node)
