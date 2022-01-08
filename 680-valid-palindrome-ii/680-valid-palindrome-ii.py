class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if reverse = string return no need to process
        if s== s[::-1]: return True
        # if len is 2 return
        if len(s)<=2: return True
        i = 0
        j = len(s)-1
        # iterate with 2 pointers from front to back and break as soon as mismatch is found 
        while i<=j:
            if s[i]!=s[j]: break
            i+=1
            j-=1
        # slice w/o i and w/o j 
        str_wo_i = s[:i]+s[i+1:]
        str_wo_j = s[:j]+s[j+1:]
        # if reverse of any w/o i and w/o j string matches return true
        # else return false
        # improvisation can be made by counting mismatch and checking even or odd
        # for odd 1 is allowd and for even 2 are allowed
        str_wo_i_r = str_wo_i[::-1]
        str_wo_j_r = str_wo_j[::-1]
        if str_wo_i == str_wo_i_r or str_wo_j == str_wo_j_r:
            return True
        else: False
        