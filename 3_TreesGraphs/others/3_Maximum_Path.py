# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:52:34 2020.

@author: 10259
"""

import numpy as np
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def CreateTree(T):
    n = np.shape(T)[0]
    # Create Nodes
    Nodes = []
    for i in range(n):
        node = TreeNode(T[i, 3])
        Nodes.append(node)

    # Establish Connections
    for i, node in enumerate(Nodes):
        left = T[i, 1] - 1
        right = T[i, 2] - 1
        if(left >= 0):
            node.left = Nodes[left]
        if(right >= 0):
            node.right = Nodes[right]

    return Nodes[0]


# This is a kind of DepthFirst Traversal
def PreorderPrint(root):
    if(root is None):
        return
    print(root.val, end=' ')
    PreorderPrint(root.left)
    PreorderPrint(root.right)


def BreadthFirst(root):
    q = Queue()
    q.put(root)
    Visited = [root]
    while(not q.empty()):
        node = q.get()
        print(node.val, end=' ')
        Visited.append(node)
        if(node.left and node.left not in Visited):
            q.put(node.left)
            Visited.append(node.left)
        if(node.right and node.right not in Visited):
            q.put(node.right)
            Visited.append(node.right)


if __name__ == '__main__':
    # first column shows the current index
    # second column shows the left child index
    # third column shows the right child index
    # fourth column shows the current value
    TMatrix = np.array([[1, 2, 3, 1], [2, 4, 5, 2],
                        [3, 6, 7, 3], [4, 0, 0, 4],
                        [5, 0, 0, 5], [6, 0, 0, 6],
                        [7, 0, 0, 7]])
    root = CreateTree(TMatrix)
    PreorderPrint(root)
    print()
    BreadthFirst(root)
