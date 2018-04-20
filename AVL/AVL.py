#!/usr/bin/env python


def height(node):
    if node is None:
        return -1
    return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class Node():
    """A node in the tree."""
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0

    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    def __str__(self):
        return '\n'.join(self._str()[0])

class AVL():
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)

    def left_heavy(self, node):
        return height(node.left) >= 2 + height(node.right)

    def right_heavy(self, node):
        return height(node.right) >= 2 + height(node.left)

    def left_balance(self, node):
        if height(node.left.left) >= height(node.left.right):
            self.right_rotate(node)
        else:
            self.left_rotate(node.left)
            self.right_rotate(node)

    def right_balance(self, node):
        if height(node.right.right) >= height(node.right.left):
            self.left_rotate(node)
        else:
            self.right_rotate(node.right)
            self.left_rotate(node)

    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def _insert(self, node, key):
        if self.root is None:
            self.root = Node(key, self.root)
            return
        else:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, node)
                else:
                    self._insert(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key, node)
                else:
                    self._insert(node.right, key)

        node.height = max(height(node.left), height(node.right)) + 1

        if (self.left_heavy(node)):
            self.left_balance(node)
        elif (self.right_heavy(node)):
            self.right_balance(node)

    def insert_tree(self, key):
        """A helper function for inserting values in tree"""
        self._insert(self.root, key)

if __name__ == '__main__': test()
