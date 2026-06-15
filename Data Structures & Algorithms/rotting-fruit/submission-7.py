class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh=0
        time=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r, c))
                if grid[r][c]==1:
                    fresh+=1


        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while fresh>0 and q:
            time+=1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr, nc))


        return time if fresh==0 else -1