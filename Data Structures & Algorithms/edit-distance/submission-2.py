class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)

        dp = [[float("inf")]*(cols+1) for _ in range(rows+1)]

        for i in range(rows+1):
            dp[i][cols] = len(word1)-i

        for j in range(cols+1):
            dp[rows][j]=len(word2)-j

        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]

                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]