"""Hash Table Class"""
from functools import reduce


class HashTable:
    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        if type(key) is not str:
            raise TypeError
        # ord return an iteger representing the unicode code point of that
        # given character
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.buckets

    def set(self, key, val):
        # insert an item at given hash key point
        self.buckets[self.hash_key(key)] = val

    def get(self, key):
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
