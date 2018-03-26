from node import Node


class LinkedList:
    """class called LinkedList """
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0

        try:
            for item in reversed(iter):
                self.insert(item)
        except TypeError:
            print('Cannot be iterated.')

    def __str__(self):
        """return all item values in singly linked list"""
        lis = []
        current = self.head
        for _ in range(self._len+1):
            lis.append(current.val)
            current = current._next
        return lis

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
