class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))
    
    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep

# Example usage
size = 10
uf = UnionFind(size)
uf.unite(1, 2)
uf.unite(3, 4)
uf.unite(3, 5)
uf.unite(5, 6)
uf.unite(7, 8)
uf.unite(8, 9)
in_same_set = (uf.find(7) == uf.find(9))
print("Are 7 and 9 in the same set?", "Yes" if in_same_set else "No")
