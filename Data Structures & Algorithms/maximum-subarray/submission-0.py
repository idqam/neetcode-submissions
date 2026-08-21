class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0 
        for x in nums:
            currSum = max(currSum, 0)
            currSum += x
            maxSum = max(currSum, maxSum)
        return maxSum
        