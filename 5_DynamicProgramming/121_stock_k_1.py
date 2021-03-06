# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 07:46:58 2020.

@author: 10259

LeetCode 121: Best time to buy and sell stock.
"""

price = [7, 1, 5, 3, 6, 4]
n = len(price)
dp_i_0 = 0
dp_i_1 = -1e10
for i in range(n):
    dp_i_0 = max(dp_i_0, dp_i_1 + price[i])
    dp_i_1 = max(dp_i_1, -price[i])
print(dp_i_0)
