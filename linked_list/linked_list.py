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
        if self.head is None:
            return 'List is empty'
        current = self.head
        while True:
            if current is None:
                break
            lis.append(current.val)
            current = current._next
        return '{}'.format(lis)

    def __len__(self):
        return self._len

    def insert(self, val):
        """insert item into the beginning of singly linked list"""
        self.head = Node(val, self.head)
        self._len += 1

    def find(self, val):
        """search if val is found in the singly linked list
            and return True or False
        """
        current = self.head
        while current is not None:
            if current.val == val:
                return True
            else:
                current = current._next
        return False

    def append(self, val):
        """
            Insert a value at the end of list
        """
        if self.head is None:
            self.head = Node(val)
            return
        current = self.head
        while current._next is not None:
            current = current._next
        current._next = Node(val)
