# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:37:06 2020

@author: 10259
"""

import numpy as np

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Print function
def PrintList(head):
    while(head):
        print(head.val,end='->')
        head = head.next
    print('NULL')
        
# Create a Linked List using elements in the list
def CreateList(array):
    dummy = ListNode()
    tail = dummy
    for val in array:
        node =ListNode(val)
        tail.next = node
        tail = node
    return dummy.next

# The length of the linked list
def ListLength(head):
    length = 0
    while(head):
        length = length + 1
        head = head.next
    return length

def ithNode(head,i,n):
    if i<=0 or i>n:
        print('out of range')
        return -1
    else:
        pointer = head
        for count in range(i-1):
            pointer = pointer.next
    return pointer

head = CreateList([1,2,3,4,5])
PrintList(head)
length = ListLength(head)
half = int(np.ceil(length/2)-1)
    
    














