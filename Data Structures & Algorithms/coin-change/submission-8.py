class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def dfs(amount):

            if amount in dp:
                return dp[amount]
            if amount==0:
                return 0

            res = float("inf")
            for coin in coins:
                if amount-coin>=0:
                    res=min(res, 1+dfs(amount-coin))

            dp[amount]=res
            return dp[amount]

        ans = dfs(amount)
        return ans if ans!=float("inf") else -1