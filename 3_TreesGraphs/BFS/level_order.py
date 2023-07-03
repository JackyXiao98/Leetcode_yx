"""
429. N-ary Tree Level Order Traversal

https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
"""

from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



def levelOrder(root: 'Node'):
    if root is None:
        return []
    queue = deque([])
    queue.append(root)
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            queue.extend(node.children)
            level.append(node.val)
        result.append(level)

    return result
