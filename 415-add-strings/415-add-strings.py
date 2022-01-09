class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)>len(num2):
            small = num2[::-1]
            big = num1[::-1]
        else:
            big= num2[::-1]
            small = num1[::-1]
        carry = 0
        cur_sum = 0
        res = ""
        for i,d in enumerate(small):
            cur_sum=carry+int(d)+int(big[i])
            if cur_sum >9:
                carry = 1
                res+=str(cur_sum%10)
            else:
                res+=str(cur_sum)
                carry = 0
        i+=1
        while i< len(big):
            #print(i)
            #print(big[i])
            cur_sum= carry+int(big[i])
            if cur_sum >9:
                carry = 1
                res+=str(cur_sum%10)
            else:
                res+=str(cur_sum)
                carry = 0
            i+=1
        if carry: res+=str(carry)
        return(res[::-1])
            
            
            
        
        