from .queue import Queue


class AnimalShelter:
    """ AnimalShelter class"""
    def __init__(self):
        self.pseudo_queue = Queue()
        self._length = 0

    def enqueue(self, obj):
        """ add either a dog or cat object """
        self.pseudo_queue.enqueue(obj)
        self._length += 1

    def dequeue(self, pref):
        """ return either the longest-waiting cat or dog"""
        pref = pref.lower()
        pref = '{}{}'.format(pref[0].upper, pref[1:])

        if type(self.pseudo_queue.dequeue()) == pref:
            return self.pseudo_queue.dequeue()

        current = self.pseudo_queue.dequeue()
        first_obj_name = current.name
        while type(current) != pref:
            self.pseudo_queue.enqueue(current)
            current = self.pseudo_queue.dequeue()

        if self.pseudo_queue.dequeue().name == first_obj_name:
            return
        while True:
            if self.pseudo_queue.dequeue().name != first_obj_name:
                self.pseudo_queue.enqueue(self.pseudo_queue.dequeue())
            break

        return current
