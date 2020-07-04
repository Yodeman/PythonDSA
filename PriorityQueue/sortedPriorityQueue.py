from PQ_Base_Class import PriorityQueueBase
from positionalList.positionallist import PositionalList

class Empty(Exception):
    pass

class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented queue implemented with a sorted list."""
    
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)
    
    def min(self):
        """Return but do not remove (k,v)tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)