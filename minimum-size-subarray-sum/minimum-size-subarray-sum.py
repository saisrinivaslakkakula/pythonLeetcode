class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==1: return 0
        min_len = float('inf')
        i =0
        j = 0
        sum_v = 0
        n = len(nums)
        while j<n:
            sum_v += nums[j]
            if sum_v < target: 
                j+=1
            else:
                while sum_v >= target and i<n:
                    #print(sum_v,target)
                    sum_v -= nums[i]
                    min_len = min(min_len,j-i+1)
                    i+=1
                j+=1
        if min_len != float('inf'): return(min_len)
        else: return 0
            
                
        
        