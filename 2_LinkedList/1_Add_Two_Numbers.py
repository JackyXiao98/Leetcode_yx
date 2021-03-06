# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:14:00 2020

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

l1 = CreateList([2,4,3])
PrintList(l1)
l2 = CreateList([5,6,4])
PrintList(l2)

dummy = ListNode()
tail = dummy
dummy1 = ListNode(0,l1)
point1 = dummy1.next
dummy2 = ListNode(0,l2)
point2 = dummy2.next
node = ListNode(0)

while(point1 and point2):
    val = point1.val + point2.val + node.val
    addOne = True if val>=10 else False
    if(not addOne):
        node.val = val
        tail.next = node
        tail = tail.next
        node = ListNode(0)
    else:
        node.val = val - 10
        tail.next = node
        tail = tail.next
        node = ListNode(1)
    point1 = point1.next
    point2 = point2.next

# point2 is empty now
while(point1):
    val = point1.val + node.val
    addOne = True if val>=10 else False
    if(not addOne):
        node.val = val
        tail.next = node
        tail = tail.next
        node = ListNode(0)
    else:
        node.val = val - 10
        tail.next = node
        tail = tail.next
        node = ListNode(1)
    point1 = point1.next
    
# point1 is empty now
while(point2):
    val = point2.val + node.val
    addOne = True if val>=10 else False
    if(not addOne):
        node.val = val
        tail.next = node
        tail = tail.next
        node = ListNode(0)
    else:
        node.val = val - 10
        tail.next = node
        tail = tail.next
        node = ListNode(1)
    point2 = point2.next
    
if(addOne):
    tail.next = node
    tail = tail.next
    
ls = dummy.next
PrintList(ls)
    



























