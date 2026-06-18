class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}
        def dfs(r, c, prev):
            
            if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c]<=prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

         
            prev = matrix[r][c]
            dp[(r, c)] =  1 + max(dfs(r+1, c, prev), dfs(r-1, c, prev), dfs(r, c+1, prev), dfs(r, c-1, prev))

            return dp[(r, c)]

        lis = 0
        for r in range(rows):
            for c in range(cols):
                lis = max(lis, dfs(r, c, float("-inf")))


        return lis