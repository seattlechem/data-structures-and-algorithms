from .queue import Queue


class AnimalShelter:
    """ AnimalShelter class"""
    def __init__(self):
        self.pseudo_queue = Queue()
        self._size = 0

    def enqueue(self, val):
        """ add either a dog or cat object """
        self.pseudo_queue.enqueue(val)

    def dequeue(self, pref):
        """ return either the longest-waiting cat or dog"""
        # change pref to only first character to upper
        # type(curret) = Cat
        if type(self.pseudo_queue.dequeue()) == pref:
            return self.pseudo_queue.dequeue()
        
        current = self.pseudo_queue.dequeue()
        while type(current) != pref:
            self.pseudo_queue.enqueue(current)
            current = self.pseudo_queue.dequeue()
        
        # another while loop to back things back to order
        
        return current
