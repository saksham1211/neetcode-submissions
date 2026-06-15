class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, prev, visit):
            if r<0 or r>=rows or c<0 or c>=cols or (r, c) in visit or heights[r][c]<prev:
                return 0

            visit.add((r, c))
            dfs(r+1, c, heights[r][c], visit)
            dfs(r-1, c,heights[r][c], visit)
            dfs(r, c+1,heights[r][c], visit)
            dfs(r, c-1,heights[r][c], visit)


        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows-1, c, heights[rows-1][c], atl)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols-1, heights[r][cols-1], atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
