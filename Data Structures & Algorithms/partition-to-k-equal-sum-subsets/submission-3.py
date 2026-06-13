class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False

        target = sum(nums)//k
        buckets = [0]*k
        nums.sort(reverse=True)

        def dfs(i):
            if i==len(nums):
                return True

            for j in range(k):
                if j>0 and buckets[j-1]==0:
                    continue
                    
                if buckets[j]+nums[i]<=target:
                    buckets[j]+=nums[i]
                    if dfs(i+1):
                        return True

                    buckets[j]-=nums[i]


            return False


        return dfs(0)