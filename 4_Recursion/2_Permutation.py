# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:52:49 2020

@author: 10259

Facebook Recursion 2.
"""

nums = [1, 2, 3]
output = []


def backtrack(combination, next_nums):
    if len(next_nums) == 0:
        output.append(combination)
        return
    else:
        for number in next_nums:
            combination.append(number)
            newcomb = combination.copy()
            combination.pop()
            set_num = set(next_nums) - {number}
            backtrack(newcomb, list(set_num))


backtrack([], nums)
