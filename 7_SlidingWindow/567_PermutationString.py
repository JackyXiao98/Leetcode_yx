# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:18:34 2020.

@author: 10259

Leetcode 567: Permutation in string.
"""

from collections import Counter


S = "ab"
T = "eidbaooo"

need = Counter(S)
window = Counter()
left, right = 0, 0
valid = 0
start = 0
length = len(S)
check = False
while right < len(T):
    c = T[right]
    right += 1
    # c is needed
    if need[c]:
        window[c] += 1
        # number of c is satisfied
        if window[c] == need[c]:
            valid += 1

    while len(need) == valid:
        # update if it's smaller
        if right - left == length:
            start = left
            check = True
        d = T[left]
        left += 1
        # d is needed but discarded
        if need[d]:
            # if number of c is not satisfied
            if window[d] == need[d]:
                valid -= 1
            # current window removes c
            window[d] -= 1

print(check)
print(length, start)
print(T[start: start+length])
