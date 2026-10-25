class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for x in nums:
            if x - 1 not in nums:
                curr = 1

                while x + 1 in nums:
                    x += 1
                    curr += 1

                best = max(curr, best)

        return best