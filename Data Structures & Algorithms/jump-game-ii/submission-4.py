class Solution:
    def jump(self, nums: List[int]) -> int:
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]

            if i>=len(nums)-1:
                return 0
        
          
            minStep = float("inf")
            for j in range(1, nums[i]+1):
                minStep = min(minStep, 1+dfs(i+j))


            dp[i]= minStep
            return dp[i]

        return dfs(0)