# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:49:03 2020.

@author: 10259

Leetcode3: no repeat.
"""

from collections import Counter

s = "abcabcbb"

left, right = 0, 0
window = Counter()
res = 0
while right < len(s):
    c = s[right]
    right += 1
    window[c] += 1

    while window[c] > 1:
        d = s[left]
        left += 1
        window[d] -= 1

    res = max(res, right-left)
