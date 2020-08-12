from PriorityQueue.Heap_PQ import HeapPriorityQueue as queue

class Tree:
    class _Node:
        def __init__(self, elem, left=None, right=None):
            self.element = elem
            self.right = right
            self.left = left
    def __init__(self, elem, right=None, left=None):
        self.root = self._Node(elem, left=left, right=right)
    def left(self):
        return self.root.left
    def right(self):
        return self.root.right

def Huffman(X):
    """
    Compress string X using Huffman algorithm.
    Return coding tree for X.
    """
    char_freq = {char:X.count(char) for char in X}
    Q = queue()
    for char in X:
        tree = Tree(char)
        Q.add(char_freq[char], tree)
    while len(Q) > 1:
        (f_1, T_1) = Q.remove_min()
        (f_2, T_2) = Q.remove_min()
        T = Tree(None, T_1, T_2)
        Q.add(f_1+f_2, T)
    (f,T) = Q.remove_min()
    return T
