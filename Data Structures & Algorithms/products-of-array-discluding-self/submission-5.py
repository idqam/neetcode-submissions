class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        right_passed = [1] * size
        left_passed = [1] * size

        i_r = 1
        i_l = 1

        for i in range(size):
            left_passed[i] = i_l
            i_l *= nums[i]
        for i in range(size - 1, -1, -1):
            
            right_passed[i] = i_r
            i_r *= nums[i]
            

        
        ans = [1] * size
        for i in range(size):
            ans[i] = right_passed[i] * left_passed[i]
        return ans