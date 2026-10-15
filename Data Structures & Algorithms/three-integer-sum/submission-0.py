class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # If the current starting number is greater than 0, 
            # a triplet summing to 0 is impossible because the array is sorted.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Sum is too small, move the left pointer to increase it
                    left += 1
                else:
                    # Sum is too large, move the right pointer to decrease it
                    right -= 1
                    
        return result