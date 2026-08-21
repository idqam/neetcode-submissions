from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #here we can turn each one into a cononical form and match 
        stt = defaultdict(list)
        for x in range(len(strs)):
            stt[''.join(sorted(strs[x]))].append(strs[x])
            
        return [stt[x] for x in stt]


        