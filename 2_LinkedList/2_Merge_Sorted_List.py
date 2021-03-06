# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:54:50 2020

@author: 10259
"""

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

l1 = CreateList([])
PrintList(l1)
l2 = CreateList([0])
PrintList(l2)

dummy = ListNode()
tail = dummy
point1 = l1
point2 = l2

while(point1 and point2):
    if(point1.val<point2.val):
        val = point1.val
        point1 = point1.next
    else:
        val = point2.val
        point2 = point2.next
    tail.next = ListNode(val)
    tail = tail.next
    
if(point1):
    tail.next = point1

if(point2):
    tail.next = point2

ls = dummy.next
PrintList(ls)
    
    
    
    
    
    
    
    
    
    
    