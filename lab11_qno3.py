class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

def is_red(node):
    return node is not None and node.color == "RED"

def rotate_left(tree, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        tree.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

def rotate_right(tree, y):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y
    x.parent = y.parent
    if y.parent is None:
        tree.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x

def fix_insertion_violations(tree, node):
    while is_red(node.parent):
        if node.parent == node.parent.parent.left:
            y = node.parent.parent.right
            if is_red(y):
                # Case 1: Recoloring
                node.parent.color = "BLACK"
                y.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    # Case 2: Left rotation
                    node = node.parent
                    rotate_left(tree, node)
                # Case 3: Recoloring and right rotation
                node.parent.color = "BLACK"
                node.parent.paren
