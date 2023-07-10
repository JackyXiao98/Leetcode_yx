class UnionFind():
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] = self.rank[rootY] + 1
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getCount(self):
        return self.count


class union_find():
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
    
    # path compression
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    # union by rank
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            rank_root_x = self.rank[root_x]
            rank_root_y = self.rank[root_y]
            if rank_root_x < rank_root_y:
                self.root[root_x] = root_y
            elif rank_root_x > rank_root_y:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] = self.rank[root_x] + 1
            self.count -= 1
        



