class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = [1] * len(nums)

        left = [1] * len(nums)
        right = [1] * len(nums)
        left_identity = 1
        right_identity = 1
        for z in range(len(nums)):
            left[z] = left_identity
            left_identity *= nums[z]
            
        for z in range(len(nums) -1, -1, -1):
            right[z] = right_identity 
            right_identity *= nums[z]
            

        ans = []
        for i in range(len(nums)):
            ans.append(right[i] * left[i])


        return ans

        
        