from PQ_Base_Class import PriorityQueueBase
from positionalList.positionallist import PositionalList

class Empty(Exception):
    pass

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        """Return Position of item with minimun key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))
    
    def min(self):
        """Return but do not remove(k,v)tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)