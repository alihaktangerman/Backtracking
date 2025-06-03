from random import randint
from copy import copy

g = [(u,v) for u in range(6) for v in range(u+1,6) if True]

class UnionFind:
    def __init__(self, size):
        """Initialize the UnionFind structure with a given size."""
        self.parent = list(range(size))  # Each element is its own parent initially
        self.rank = [0] * size          # Rank for union by rank optimization
    
    def find(self, x):
        """Find the root of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """Union the sets containing x and y using union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return  # Already in the same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
    
    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

uf = UnionFind(6)
tree = []

counter = 0

def solve(g):
    global counter
    e = None
    for edge in g:
        if not uf.connected(edge[0],edge[1]):
            e = edge
    if not e:
        if len(tree) == 5:
            print(tree)
            counter += 1
        return
    prev_parent = copy(uf.parent)
    prev_rank = copy(uf.rank)
    uf.union(e[0],e[1])
    tree.append(e)
    solve(g)
    tree.pop()
    uf.rank = prev_rank
    uf.parent = prev_parent
    g.pop(g.index(e))
    solve(g)
    g.append(e)            
solve(g)

print(counter)