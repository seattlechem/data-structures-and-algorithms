from .node import Node


class AnimalShelter:
    """ AnimalShelter class"""
    def __init__(self):
        self._size = 0

    def enqueue(self, val):
        """ add either a dog or cat object """
        self.push(val)

    def dequeue(self, val):
        """ return either the longest-waiting cat or dog"""
        pass
