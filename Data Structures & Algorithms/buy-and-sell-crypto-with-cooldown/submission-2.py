class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp ={}
        def dfs(i, buying):
            if (i, buying) in dp:
                return dp[(i, buying)]

            if i>=len(prices):
                return 0 

            profit = dfs(i+1, buying)
            if buying:
                profit=max(profit, -prices[i]  + dfs(i+1, not buying))

            else:
                profit=max(profit, prices[i]+dfs(i+2, not buying))

            dp[(i, buying)] = profit
            
            return dp[(i, buying)]

        return dfs(0, True)