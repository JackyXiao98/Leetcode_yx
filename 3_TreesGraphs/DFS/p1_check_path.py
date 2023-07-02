"""

1971. Find if Path Exists in Graph

https://leetcode.com/problems/find-if-path-exists-in-graph/description/
"""


# Start a dfs from source, check if destination can be reached.
from collections import defaultdict


def validPath(n: int, edges, source: int, destination: int) -> bool:
    # 1 <= n <= 10^5, creating an adjacency matrix is too large, it's sparse, 
    # we will use link list to represent the graph
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    # We need to check if a node is vistied or not
    visited = {i:False for i in range(n)}
    found = False

    def dfs(node):
        nonlocal graph, visited, found
        visited[node] = True
        # print(node, destination)
        if node == destination:
            found = True
            # print(found)
            return
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)

    dfs(source)
    return found

if __name__ == '__main__':

    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0 
    destination = 2

    found = validPath(n, edges, source, destination)
    print(found)
