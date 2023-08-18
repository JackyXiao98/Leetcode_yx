"""

542: 0 1 matrix.

https://leetcode.com/problems/01-matrix/description/
"""



class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        from collections import deque
        import numpy as np
        m = len(mat)
        n = len(mat[0])

        visited = [[False]*n for _ in range(m)]
        distance = [[10**6]*n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    distance[i][j] = 0
                    queue.append((i, j, 0))

        def is_valid(i, j, m, n):
            if 0 <= i < m and 0 <= j < n:
                return True
            else:
                return False

        while len(queue) > 0:
            length = len(queue)
            for _ in range(length):
                # same level
                i, j, dist = queue.popleft()
                # visited[i][j] = True
                distance[i][j] = dist
                for di, dj in directions:
                    if is_valid(i+di, j+dj, m, n) and (not visited[i+di][j+dj]):
                        queue.append((i+di, j+dj, dist+1))
                        visited[i+di][j+dj] = True

        return distance
