class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inc_val = digits[-1]+1
        if inc_val <9 : digits[-1] = inc_val
        else:
            rev_dig = digits[::-1]
            carry = 0
            i=0
            while i<len(rev_dig):
                inc_val = rev_dig[i]+1
                if inc_val >9:
                    rev_dig[i] = inc_val %10
                    carry = 1
                else:
                    rev_dig[i] = inc_val
                    carry = 0
                    break
                i+=1
            if carry: rev_dig.append(1)
            digits = rev_dig[::-1]
        return digits
            
        