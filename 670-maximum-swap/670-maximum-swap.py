class Solution:
    def findnextmax(self,n,i,num):
        j = len(num)-1
        max_ = n
        max_i = i
        while j>i:
            if num[j] > max_: 
                max_ = num[j]
                max_i = j
            j-=1
        return max_i if max_>n else None
    def maximumSwap(self, num: int) -> int:
        if num <= 9: return num
        str_num = str(num)
        num = [int(n) for n in str_num]
        #print(num)
        for i,n in enumerate(num):
            max_i = self.findnextmax(n,i,num)
            #print(max_i)
            if max_i:
                #print("max:",num[max_i])
                num[max_i], num[i] = num[i],num[max_i]
                break
        num = [str(n) for n in num]
        num = "".join(num)
        num = int(num)
        return(num)
                
        