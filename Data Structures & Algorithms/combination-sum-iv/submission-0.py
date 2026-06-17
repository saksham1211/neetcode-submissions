class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, target):
            if (i, target) in dp:
                return dp[(i, target)]

            if target==0:
                return 1
            if target<0:
                return 0
                
            if i>=len(nums):
                return 0

            ways = 0
            for j in range(len(nums)):
                ways+=dfs(j, target-nums[j])

            dp[(i, target)]=ways

            return dp[(i, target)]



        return dfs(0, target)
