from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in h:
                return [h[diff], i]
            else:
                h[nums[i]] = i 
        return [] 
        