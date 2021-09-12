import numpy as np

def validPath(n: int, edges, start: int, end: int) -> bool:
    # build graph connection matrix
    is_connected = np.zeros([n, n])
    for edge in edges:
        i, j = edge
        is_connected[i, j] = 1
        is_connected[j, i] = 1
    is_visited = [0] * n
    
    def dfs(i, is_connected):
        is_visited[i] = 1
        for k in range(n):
            if is_connected[i][k] == 1:
                if is_visited[k] == 0:
                    dfs(k, is_connected)
    
    dfs(start, is_connected)
    
    return (is_visited[end] == 1)


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    start = 0
    end = 5
    print(validPath(n, edges, start, end))
