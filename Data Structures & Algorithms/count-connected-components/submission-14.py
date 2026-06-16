class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, n):
        curr = n
        while curr!=self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]

        return curr

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1==p2:
            return False

        if self.rank[p1]>self.rank[p2]:
            self.parent[p2]=p1
            self.rank[p1]+=self.rank[p2]

        else:
            self.parent[p1]=p2
            self.rank[p2]+=self.rank[p1]

        return True

        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        res=n
        for u, v in edges:
            if dsu.union(u, v):
                res-=1

        return res