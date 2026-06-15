class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(list)
        outdegree = defaultdict(list)

        for u, v in trust:
            indegree[v].append(u)
            outdegree[u].append(v)

        for v in indegree:
            if v not in outdegree and len(indegree[v])==n-1:
                return v
        
        return -1