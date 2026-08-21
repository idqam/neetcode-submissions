class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left, right = [1] * len(nums), [1] * len(nums)
        
        left_accumulator = 1
        right_accumulator = 1



        for i in range(len(nums)):
            left[i] = left_accumulator
            left_accumulator *= nums[i]
        

        for i in range(len(nums)-1, -1,-1):
            right[i] = right_accumulator
            right_accumulator *= nums[i]
        
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = right[i] * left[i]
        

        return ans




        