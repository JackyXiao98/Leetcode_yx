# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:15:42 2020

@author: 10259
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def CreateTree():
    root = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n3 = TreeNode(3)
    n7 = TreeNode(7)
    root.left = n1
    root.right = n6
    n6.left = n3
    n6.right = n7
    return root

def InorderTraversal(root,array):
    if(root==None):
        return
    InorderTraversal(root.left,array)
    array.append(root.val)
    InorderTraversal(root.right,array)
    
def isValid(array):
    length = len(array)
    if(length<2):
        return True
    i = 0
    while(i<length-1):
        if(array[i]<array[i+1]):
            flag = 1
        else:
            flag = 0
            break
        i = i+1
    if(flag==0):
        return False
    else:
        return True

if __name__ == '__main__':
    root = CreateTree()
    array = []
    InorderTraversal(root,array)
    print(isValid(array))
        
