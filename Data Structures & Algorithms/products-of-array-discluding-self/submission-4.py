class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prods, right_prods = [1] * (len(nums)), [1] * (len(nums) )

        left_identity  = 1
        right_identity = 1


        ans = [1] * len(nums)
        for i in range(len(nums)):
            left_prods[i] = left_identity
            left_identity *= nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            right_prods[i] = right_identity
            right_identity *= nums[i]
            

        for i in range(len(ans)):
            ans[i] = left_prods[i] * right_prods[i]


        return ans
        