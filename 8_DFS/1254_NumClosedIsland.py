# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:56:44 2020.

@author: 10259

Leetcode 1254: Number of closed island
"""

grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]

global closed
global count

def dfs(i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        global closed
        closed = False
        return
    if grid[i][j] != 0:
        return
    grid[i][j] = -1
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i-1, j)
    dfs(i+1, j)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            global closed
            closed = True
            dfs(i, j)
            if closed:
                count = count + 1