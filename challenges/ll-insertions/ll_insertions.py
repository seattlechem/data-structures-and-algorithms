class Node:
"""class called Node """
def __init__(self, val, next=None):
    self.val = val
    self._next = next

def __str__(self):
    return '{val}'.format(val=self.val)


class LinkedList:
    """class called LinkedList """
    def __init__(self, iter=[]):
        self.head = None
        self._len = 0

        try:
            for item in reversed(iter):
                self.insert(item)
        except TypeError:
            raise TypeError('It\'s not a iterable type.')

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
    
    def append(self, val):
        """
        Insert a value at the end of list
        """"
        if self.head is None:
            self.head = Node(val)
            return
        current = self.head
        while current_next is not None:
            current = current_next
        # when you reach to the end where _next is none
        current_next = Node(val)
        

