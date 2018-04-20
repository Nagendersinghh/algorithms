class BSTNode(object):
    """A binary search tree node."""
    def __init__(self, parent, key):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node"""
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def find(self, key):
        if self.key == key:
            return self
        elif key < self.key:
            return self.left.find(key)
        else:
            return self.right.find(key)

    def find_min(self):
        if self.left is None:
            return self
        return self.left.find_min()

    def successor(self, key):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.successor()
            self.key, s.key = s.key, self.key
            return s.delete()


class MinBSTNode(BSTNode):
    """An augmented BSTNode which keeps track of the node with the minimum
    key in the subtree rooted at this node"""
    def __init__(self, parent, key):
        super(MinBSTNode, self).__init__(parent, key)
        self.min = self

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            self.min = node
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def find_min(self):
        return self.min

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
                    self.parent.min = self.parent.left.min
                else:
                    self.parent.min = self.parent
                c = self.parent
                while c.parent is not None and c is c.parent.left:
                    c.parent.min = c.min
                    c = c.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.successor()
            self.key, s.key = s.key, self.key
            return s.delete()


class BST(object):
    """A binary search tree."""
    def __init__(self, klass=BSTNode):
        self.root = None
        self.klass = klass

    def insert(self, k):
        node = self.klass(None, k)

        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def inorder_walk(self):
        if self.root is None:
            return
        self._inorder_walk(self.root)

    def _inorder_walk(self, node):
        if node is None:
            return
        self._inorder_walk(node.left)
        print(node.key)
        self._inorder_walk(node.right)

    def find(self, key):
        return self.root and self.root.find(key)

    def find_min(self):
        if self.root is None:
            return
        return self.root.find_min()

    def delete(self, key):
        node = self.find(key)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = self.klass(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def successor(self, key):
        """Find and return the node with next larger key"""
        node = self.find(key)
        return node and node.successor(key)


class MinBST(BST):
    """An augmented BST that keeps track of the node with minimum key"""
    def __init__(self):
        super(MinBST, self).__init__(MinBSTNode)

