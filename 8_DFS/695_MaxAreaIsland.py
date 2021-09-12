# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:29:36 2020.

@author: 10259

Leetcode 695: Max area of island.
"""

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
cur_area


def dfs(i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) \
            or grid[i][j] != 1:
        return
    else:
        global cur_area
        cur_area = cur_area + 1
        grid[i][j] = 0
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i+1, j)
    dfs(i-1, j)


max_area = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            global cur_area
            cur_area = 0
            dfs(i, j)
            if cur_area > max_area:
                max_area = cur_area
