# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:22:11 2020.

@author: 10259

Leetcode 1249
"""


s = '))(('
stack = []
index_to_remove = set()

for i, c in enumerate(s):
    if c not in '()':
        continue
    if c == '(':
        stack.append(i)
    elif not stack:
        index_to_remove.add(i)
    else:
        stack.pop()

index_to_remove = index_to_remove.union(set(stack))
string_builder = []
for i, c in enumerate(s):
    if i not in index_to_remove:
        string_builder.append(c)

print("".join(string_builder))
