class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def height(node):
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(node):
    if not node:
        return True

    left_height = height(node.left)
    right_height = height(node.right)

    # Check if the current node is balanced
    if abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True

    return False

# Example usage:
# Construct an AVL tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)

# Check if the AVL tree is balanced
if is_balanced(root):
    print("The AVL tree is balanced.")
else:
    print("The AVL tree is not balanced.")
