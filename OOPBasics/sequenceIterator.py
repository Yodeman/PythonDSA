class SequenceIterator:
    """An iterator for any python sequence type"""
    def __init__(self, seq):
        self._seq = seq
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def __len__(self):
        return len(self._seq)

if __name__ == "__main__":
    X = SequenceIterator([1,2,3,4,5,6])
    for i in range(len(X)):
        print(next(X), end=' ')