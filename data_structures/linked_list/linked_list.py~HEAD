import pytest
from .node import Node


class LinkedList:
    """class called LinkedList """
    def __init__(self, iter=[]):
        self.head = None
        self._len = 0
        if not isinstance(iter, (str, tuple, list)):
            raise TypeError('It\'s not an iterable type.')
        for item in reversed(iter):
            self.insert(item)
            

    def __str__(self):
        """return all item values in singly linked list"""
        lis = []
        if self.head is None:
            return 'List is empty'
        current = self.head
        while current:
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
        while current:
            if current.val == val:
                return True
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
        while current._next:
            current = current._next
        current._next = Node(val)

    def insert_before(self, val, new_val):
        """ add a new node with the given new_value immediately before the
        first value node """
        current = self.head
        if val > len(self):
            raise ValueError('Position to add is incorrect.')
        while current._next.val != val:
            current = current._next
        current._next = Node(new_val, current._next)

    def insert_after(self, val, new_val):
        """
        .insertAfter(value, newVal) which add a new node with the given
        newValue immediately after the first value node
        """
        current = self.head
        if val > len(self):
            raise ValueError('Position to add is incorrect.')
        while current.val != val:
            current = current._next
        current._next = Node(new_val, current._next)

    def kth_from_end(self, k):
        """ takes a number, k, as an argument. Return the node
        that is k from the end of the linked list."""
        length = len(self)
        if type(k) != int:
            raise TypeError('Use only number.')
        if k >= length:
            raise ValueError('It goes over the range.')
        
        counter = 0
        current = self.head
        while counter != length - (k + 1):
            print(counter)
            current = current._next
            counter += 1
        return current

    def has_loop(self):
        '''
        It returns True if linked list contains a loop;
        False if there is no loop present in the
        linked list
         '''
        slow = self.head
        fast = self.head

        while fast._next and fast._next._next:
            slow = slow._next
            fast = fast._next._next
            if slow == fast:
                return True
            pass
        return False
