class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        count = 1
        ans = 0
        for x in nums:
            if x - 1 not in nums:
                run = 1
                candidate = x + 1
                while candidate in nums:
                    run += 1
                    candidate = candidate + 1
                ans = max(run, ans)
        return ans
        