from node import Node


class LinkedList:
    """class called LinkedList """
    def __init__(self, iter=[]):
        self.head = None
        self._len = 0

        try:
            for item in reversed(iter):
                self.insert(item)
        except TypeError:
            print('It\'s not a iterable type.')

    def __str__(self):
        """return all item values in singly linked list"""
        lis = []
        current = self.head
        for _ in range(self._len+1):
            lis.append(current.val)
            current = current._next
        return lis

    def insert(self, val):
        """insert item to singly linked list"""
        self.head = Node(val, self.head)
        self._len += 1

    def find(self, val):
        """search if val is found in the singly linked list
            and return True or False
        """
        current = self.head
        while current is not None:
            if current.val = val:
                return True
            else:
                current = current._next
        return False
