"""Hash Table Class."""
from .linked_list import LinkedList as LL


class HashTable:
    """Class definitions."""

    def __init__(self, max_size=1024):
        """Make an instance of HashTable."""
        if type(max_size) is not int:
            raise TypeError('Max size must be integer.')

        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def hash_key(self, key):
        """Obtain the hashed key."""
        if type(key) is not str:
            raise TypeError('key must be string.')

        sum = 0
        for char in key:
            sum += ord(char)

        return sum % len(self.buckets)

    def set(self, key, val):
        """Insert into hash table."""
        self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        """Retrieve the value."""
        current = self.buckets[self.hash_key(key)].head

        while current:
            for item in current.val.keys():
                item == key
                return current.val[item]
            current = current._next

        return False

    def remove(self, key):
        """Reset the bucket containing the key."""
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
