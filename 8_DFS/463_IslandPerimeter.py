# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:01:30 2020.

@author: 10259

Leetcode 463: IslandPerimeter.
"""

# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
grid = [[0, 1]]
global count


def dfs(i, j):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
        global count
        count = count + 1
        return
    if grid[i][j] != 1:
        if grid[i][j] == 0:
            count = count + 1
            return
        else:
            return
    else:
        grid[i][j] = -1
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i-1, j)
    dfs(i+1, j)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            global count
            count = 0
            dfs(i, j)
            if count > 0:
                print(count)
