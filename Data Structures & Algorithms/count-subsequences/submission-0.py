class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows = len(s)
        cols = len(t)

        dp = [[0]*(cols+1) for _ in range(rows+1)]

        for i in range(rows+1):
            dp[i][cols] = 1

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i]==t[j]:
                    dp[i][j]+=dp[i+1][j+1]

        return dp[0][0]