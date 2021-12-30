class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0: return 0
        max_l = 0
        i = 0
        j = 0
        dist = {}
        while j<len(s):
            dist[s[j]] = j
            if len(dist) >k:
                min_idx = min(dist.values())
                i = min_idx+1
                del dist[s[min_idx]]
            max_l = max(max_l,j-i+1)
            j+=1
        return(max_l)
        