class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        minHeap = [[grid[0][0], 0, 0]]

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
                
            if (r, c) ==(n-1, n-1):
                return t
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr in range(n) and nc in range(n) and (nr, nc) not in visit:
                    heapq.heappush(minHeap, [max(t, grid[nr][nc]), nr, nc])

            