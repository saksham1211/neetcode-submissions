class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        adj = defaultdict(list)
        res=[]

        for u, v in prerequisites:
            indegree[u]+=1
            adj[v].append(u)

        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        while q:
            crs = q.popleft()
            res.append(crs)
            for nei in adj[crs]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return res if len(res)==numCourses else []
