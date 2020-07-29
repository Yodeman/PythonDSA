from BST import TreeMap

class SplayTreeMap(TreeMap):
    """Sorted map implementation using a splay tree."""

    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand_p = self.parent(parent)
            if grand_p is None:
                # Zig case
                self._rotate(p)
            elif (parent==self.left(grand_p))==(p==self.left(parent)):
                # zig-zig case
                self._rotate(parent)
                self.rotate(p)
            else:
                # zig-zag case
                self._rotate(p)
                self._rotate(p)

    def _rebalance_access(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)
            
    def _rebalance_insert(self, p):
        self._splay(p)