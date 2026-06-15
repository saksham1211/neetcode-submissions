class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        res=set()
        adj=defaultdict(list)
        for u, v in prerequisites:
            indegree[u]+=1
            adj[v].append(u)
      
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        while q:
            crs = q.popleft()
            res.add(crs)
            for nei in adj[crs]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)


        return len(res)==numCourses