class Solution:
    def findMax(self,num_l,l):
        j = len(num_l)-1
        max_d = -1
        max_i = None
        #print(l)
        while(j>l):
            
            if num_l[j] > max_d:
                #print("sada")
                max_d = num_l[j]
                max_i = j
            j-=1
        if max_i and num_l[max_i] > num_l[l]: return max_i
        else: return None
    def maximumSwap(self, num: int) -> int:
        num_l = [int(x) for x in str(num)]
        for i,n in enumerate(num_l):
            max_i = self.findMax(num_l,i)
            if max_i:
                num_l[i],num_l[max_i] = num_l[max_i],num_l[i]
                break
        strings = [str(num_l) for num_l in num_l]
        a_string = "".join(strings)
        an_integer = int(a_string)
        return(int(an_integer))
            
            
        