class Node:
    def __init__(self, key, color, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color="BLACK")
        self.root = self.NIL

    def insert(self, key):
        # Perform a regular BST insert
        new_node = Node(key, color="RED")
        self._insert(new_node)

        # Fix Red-Black tree properties
        self._insert_fixup(new_node)

    def _insert(self, new_node):
        # Perform a regular BST insert
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def _insert_fixup(self, node):
        # Fix the Red-Black tree properties after insertion
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                # Symmetric case
                # (same as above with "left" and "right" exchanged)
                pass

        self.root.color = "BLACK"

    def _left_rotate(self, x):
        # Left rotation of nodes in Red-Black tree
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        # Right rotation of nodes in Red-Black tree
        pass
 
