# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:44:19 2020

@author: 10259
"""

s = 'abcabcab'
s1 = 'pwwkew'
check = []
count = 0
for c in s1:
    if c in check:
        check = check[check.index(c)+1:]
    check.append(c)
    count = max(count,len(check))
print(count)

