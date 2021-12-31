class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        invalid = 0
        for c in counter:
            if (counter[c]%2) !=0: invalid+=1
        if invalid >1: return False
        else: return True
        