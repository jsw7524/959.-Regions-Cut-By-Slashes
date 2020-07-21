class UnionFind(object):
    def __init__(self, size):
        self.parent = []
        self.rank = []
        self.count = size
        for i in range(0, size):
            self.parent.append(i)
            self.rank.append(0)

    def find(self, i):
        # with path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def connected(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        p = self.find(i)
        q = self.find(j)
        if p == q: return
        if self.rank[p] < self.rank[q]:
            self.parent[p] = q
        elif self.rank[p] > self.rank[q]:
            self.parent[q] = p
        else:
            self.parent[q] = p
            self.rank[p] += 1
        self.count -= 1

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n=len(grid)
        uf=UnionFind(4*n*n)
        for row in range(n):
            for col in range(n):
                smbl=grid[row][col]
                i=4*(row*n+col)
                if smbl == " ":
                    uf.union(i,i+1)
                    uf.union(i+1,i+2)
                    uf.union(i+2,i+3)
                    uf.union(i+3,i)
                elif smbl == "/":
                    uf.union(i+1,i+2)
                    uf.union(i+3,i)
                else:
                    uf.union(i+1,i)
                    uf.union(i+3,i+2)
                    
        for row in range(n):
            for col in range(n-1):
                i=4*(row*n+col)
                j=4*(row*n+(col+1))
                uf.union(i+1,j+3)

        for row in range(n-1):
            for col in range(n):
                i=4*(row*n+col)
                j=4*((row+1)*n+col)
                uf.union(i+2,j)
        return uf.count
                
sln=Solution()
assert 5==sln.regionsBySlashes(["/\\","\\/"])
assert 4==sln.regionsBySlashes(["\\/","/\\"])
assert 1==sln.regionsBySlashes([" /","  "])
assert 2==sln.regionsBySlashes([" /","/ "])
assert 2==sln.regionsBySlashes(["/"])        
        
