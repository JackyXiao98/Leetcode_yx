# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:06:25 2020.

@author: 10259

Leetcode 226: invert binary tree
"""


class TreeNode:
    """Tree Definition."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree():
    """Tree Definition."""
    root = TreeNode(4)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    root.left = n2
    root.right = n7
    n2.left = TreeNode(1)
    n2.right = TreeNode(3)
    n7.left = TreeNode(6)
    n7.right = TreeNode(9)
    return root


def invertTree(root: TreeNode) -> TreeNode:
    """Tree Invert."""
    if root is None:
        return
    root.right, root.left = root.left, root.right
    invertTree(root.left)
    invertTree(root.right)


def printTree(root):
    """Tree Print."""
    if(root is None):
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)


root = createTree()
invertTree(root)
printTree(root)
