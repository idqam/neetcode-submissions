class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sequence = set()
        ans = 0
        curr = 0
        nums = set(nums)
        i = 1
        for x in nums:
            if x - 1 not in nums:
                while x + i  in nums:

                    sequence.add(x + i)
                    curr += 1
                    i += 1
            
            ans = max(curr, ans)
            i = 1
            curr = 0

        return ans + 1

        