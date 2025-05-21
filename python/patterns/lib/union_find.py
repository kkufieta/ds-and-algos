class UnionFind:
    def __init__(self, n=0):
        self.parent = [v for v in range(n+1)]
        self.rank = [1] * (n+1)

    def find(self, x):
        xp = x
        while self.parent[xp] != xp:
            xp = self.parent[xp]
        while self.parent[x] != x:
            tmp = self.parent[x]
            self.parent[x] = xp
            self.rank[x] = 1
            x = tmp
        return xp
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.parent[x] = y
            self.rank[y] += self.rank[x]