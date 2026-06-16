class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x2-x1)+abs(y2-y1)

                adj[(x1, y1)].append((dist, (x2, y2)))
                adj[(x2, y2)].append((dist, (x1, y1)))

        x, y = points[0]
        minHeap = [(0, (x, y))]
        visit = set()
        res=0
        while minHeap:
            cst, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res+=cst
            for nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, nei)

        return res