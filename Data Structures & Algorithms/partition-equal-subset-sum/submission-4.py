class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False

        dp = {}
        def dfs(i, target):
            if (i, target) in dp:
                return dp[(i, target)]

            if i>=len(nums):
                return target==0

            
            if target<0:
                return False


            dp[(i, target)] =  dfs(i+1, target) or dfs(i+1, target-nums[i])
            return dp[(i, target)]


        return dfs(0, sum(nums)//2)