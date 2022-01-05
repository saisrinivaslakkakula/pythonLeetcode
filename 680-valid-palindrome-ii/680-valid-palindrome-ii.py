class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s== s[::-1]: return True
        if len(s)<=2: return True
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i]!=s[j]: break
            i+=1
            j-=1
        str_wo_i = s[:i]+s[i+1:]
        str_wo_j = s[:j]+s[j+1:]
        str_wo_i_r = str_wo_i[::-1]
        str_wo_j_r = str_wo_j[::-1]
        if str_wo_i == str_wo_i_r or str_wo_j == str_wo_j_r:
            return True
        else: False
        