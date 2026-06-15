class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r, c, 0))

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                dist+=1
                for dr, dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc]==2147483647:
                        grid[r+dr][c+dc] = dist
                        q.append((r+dr, c+dc, dist))


                        