class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = 0
        closed_c = 0
        for c in s:
            if c =="(": open_c+=1
            if c ==')':
                if open_c >0: open_c -=1
                else: closed_c +=1
        return(open_c+closed_c)