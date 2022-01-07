class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i= len(num1)-1
        j = len(num2)-1
        cur_sum = 0
        carry = 0
        sum_s =""
        while i>=0 and j >=0:
            #print(i,j)
            cur_sum = int(num1[i])+int(num2[j])+carry
            if cur_sum >9:
                sum_s += str(cur_sum%10)
                carry = 1
            else:
                sum_s += str(cur_sum)
                carry = 0
            i-=1
            j-=1
        while i>=0:
            cur_sum = int(num1[i])+carry
            if cur_sum >9:
                sum_s += str(cur_sum%10)
                carry = 1
            else:
                sum_s += str(cur_sum)
                carry = 0
            i-=1
        while j>=0:
            cur_sum = int(num2[j])+carry
            if cur_sum >9:
                sum_s += str(cur_sum%10)
                carry = 1
            else:
                sum_s += str(cur_sum)
                carry = 0
            j-=1
        if carry: sum_s +="1"
        return(sum_s[::-1])
        