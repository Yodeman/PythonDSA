from abc import ABCMeta, abstractmethod
import collections

class Sequence(metaclass=ABCMeta):

    @abstractmethod             # ensures sublclass overides it else raises error.
    def __len__(self):
        """Return length of sequence"""
    
    @abstractmethod
    def __getitem__(self, j):
        """Return element at index j of sequence"""

    def __contains__(self, val):
        """Return True if val in the sequence else false"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        """Return the number of element equal to val"""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
