from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = defaultdict(int)
        max_heap = []
        ans = []
        for x in nums:
            freqs[x] += 1
        
        for x in freqs:
            
            heapq.heappush(max_heap, (-freqs[x], x))
        print(max_heap)
        for _ in range(k):
            a, b = heapq.heappop(max_heap)
            ans.append(b)
        return ans


        
        
