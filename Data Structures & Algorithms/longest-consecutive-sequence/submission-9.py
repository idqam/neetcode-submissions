class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        count = 0
        nums = set(nums)

        for x in nums:
            if x - 1 not in nums:
                recent = 0
                
                while x in nums:
                    x = x + 1
                    recent += 1
                count = max(recent, count)
                    
        return count
        