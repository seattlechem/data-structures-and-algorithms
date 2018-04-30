"""Hash Table Class"""
from functools import reduce
from .linked_list import LinkedList as LL


class HashTable:
    def __init__(self, max_size=1024):
        """Make an instance of HashTable"""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def hash_key(self, key):
        """Obtain the hashed key"""
        if type(key) is not str:
            raise TypeError
        # ord return an iteger representing the unicode code point of that
        # given character
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.buckets

    def set(self, key, val):
        """Insert into hash table"""
        # insert an item at given hash key point
        self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
