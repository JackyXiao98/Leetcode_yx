# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:18:34 2020.

@author: 10259

Leetcode 76: minimal window substring.
"""

from collections import Counter

# S = "ADOBECODEBANC"
# T = "ABC"
S = "AAB"
T = "AAB"

need = Counter(T)
window = Counter()
left, right = 0, 0
valid = 0
start = 0
length = 1e10
while right < len(S):
    c = S[right]
    right += 1
    # c is needed
    if need[c]:
        window[c] += 1
        # number of c is satisfied
        if window[c] == need[c]:
            valid += 1

    while len(need) == valid:
        # update if it's smaller
        if right - left < length:
            start = left
            length = right - left
        d = S[left]
        left += 1
        # d is needed but discarded
        if need[d]:
            # if number of c is not satisfied
            if window[d] == need[d]:
                valid -= 1
            # current window removes c
            window[d] -= 1


print(length, start)
print(S[start: start+length])
