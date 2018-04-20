import bst


class AVL(bst.BST):
    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def updateHeight(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if (node.right is not None):
            node.right.parent = node
        if (node is node.parent.right):
            node.parent.right = y
        else:
            node.parent.left = y
        y.parent = node.parent
        y.left = node
        node.parent = y
        self.updateHeight(y)
        self.updateHeight(node)

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if (node.left is not None):
            node.left.parent = node
        if node is node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.parent = node.parent
        y.right = node
        node.parent = y
        self.updateHeight(y)
        self.updateHeight(node)

    def rebalance(self, node):
        while node is not None:
            self.updateHeight(node)
            # Left heavy
            if self.height(node.left) > 1 + self.height(node.right):
                if self.height(node.left.right) > self.height(node.left.left):
                    self.left_rotate(node.left)
                    self.right_rotate(node)
                else:
                    self.right_rotate(node)
            # Right heavy
            elif self.height(node.right) > 1 + self.height(node.left):
                if self.height(node.right.left) > self.height(node.right.right):
                    self.right_rotate(node.right)
                    self.left_rotate(node)
                else:
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        node = super(AVL, self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        node = super(AVL, self).delete(k)
        self.rebalance(node.parent)
