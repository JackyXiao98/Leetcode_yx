# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:22:11 2020.

@author: 10259

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

1249. Minimum Remove to Make Valid Parentheses

"""


s = '))(('


stack = []
index_to_remove = set()

for i, c in enumerate(s):
    if c not in '()':
        continue
    if c == '(':
        # only keep '(' in the stack
        stack.append(i)
    elif not stack:
        # current ')' doesn't have a '(' pair
        index_to_remove.add(i)
    else:
        # current ')' has a valid pair, remove '('
        stack.pop()

# the remaining '(' doesn't have a ')' pair
index_to_remove = index_to_remove.union(set(stack))
string_builder = []
for i, c in enumerate(s):
    if i not in index_to_remove:
        string_builder.append(c)

print("".join(string_builder))
