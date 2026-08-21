class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_counter = 0

        for x in seen:
            if x - 1 not in seen:  # x is a sequence start
                current_len = 1
                next_cand = x + 1
                while next_cand in seen:
                    current_len += 1
                    next_cand += 1
                max_counter = max(max_counter, current_len)

        return max_counter