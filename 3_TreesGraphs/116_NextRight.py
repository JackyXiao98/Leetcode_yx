class TreeNode:
    """Tree Definition."""

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def createTree():
    """Tree Definition."""
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    n2.left = TreeNode(4)
    n2.right = TreeNode(6)
    n3.left = TreeNode(6)
    n3.right = TreeNode(7)
    return root


def connectTwoNode(node1, node2):
    """Connect two adjacent nodes."""
    if node1 is None or node2 is None:
        return
    node1.next = node2
    connectTwoNode(node1.left, node1.right)
    connectTwoNode(node2.left, node2.right)
    connectTwoNode(node1.right, node1.left)


def connect(root):
    """Connect each node with its right adjacency."""
    if root is None:
        return None
    connectTwoNode(root.left, root.right)
    return root