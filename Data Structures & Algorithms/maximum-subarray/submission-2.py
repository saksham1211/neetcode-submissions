class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray = nums[0]
        currSum=0
        for n in nums:
            currSum+=n
            subarray = max(subarray, currSum)

            if currSum<0:
                currSum=0

        return subarray