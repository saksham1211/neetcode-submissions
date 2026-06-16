class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for src, dst, t in times:
            adj[src].append([t, dst])

        visit=set()
        minHeap = [[0, k]]
        res=0
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            res=t
            for nei in adj[node]:

                heapq.heappush(minHeap, [t+nei[0], nei[1]])


        return res if len(visit)==n else -1
