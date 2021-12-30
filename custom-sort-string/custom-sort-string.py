from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_idx = {}
        for i,char in enumerate(order):
            order_idx[char] = i
        
        lc = Counter(s)
        s = ""
        for ordchar in order_idx:
            if ordchar in lc:
                s+=ordchar*lc[ordchar]
        for char in lc:
            if char not in order_idx:
                s+= char*lc[char]
        return(s)
        
                
            
        