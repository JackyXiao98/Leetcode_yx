# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:00:31 2020.

@author: 10259

Leetcode 54: Spiral Matrix.
"""

import numpy as np

matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
res = []
matrix = np.array(matrix)


def boundary(mat, res):
    m = len(mat)
    n = len(mat[0])
    for i in range(n):
        res.append(mat[0][i])
        # print(i)
    if m > 1:
        for j in range(1, m):
            res.append(mat[j][n-1])
            # print(j)
        if n > 1:
            for k in range(n-2, -1, -1):
                res.append(mat[m-1][k])
            for s in range(m-2, 0, -1):
                res.append(mat[s][0])
    return


row_top = 0
row_down = len(matrix)
col_left = 0
col_right = len(matrix[0])
while(row_top < row_down and col_left < col_right):
    mat = matrix[row_top: row_down, col_left: col_right]
    boundary(mat, res)
    row_top = row_top + 1
    row_down = row_down - 1
    col_left = col_left + 1
    col_right = col_right - 1
    print(row_top, row_down, col_left, col_right)
print(res)
