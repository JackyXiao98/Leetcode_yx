# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:45:33 2020.

@author: 10259

Leetcode: Number Sum.
"""

N = 15

cur_sum = 0
low = 1
high = 1
total_count = 0
res = []
while high <= N:
    while cur_sum < N:
        cur_sum = cur_sum + high
        high = high + 1

    while cur_sum >= N:
        if cur_sum == N:
            res.append([low, high])
            total_count = total_count + 1
        cur_sum = cur_sum - low
        low = low + 1
