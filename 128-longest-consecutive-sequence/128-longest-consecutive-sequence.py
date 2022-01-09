class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums) == 1: return 1
        set_num = set(nums)
        nums = list(set_num)
        nums.sort()
        i=0
        prev_seq = 0
        seq = 1
        print(nums)
        for j in range(1,len(nums)):
            #print(nums[j],nums[i],nums[j]-nums[i])
            if nums[j] - nums[i] ==1: 
                seq+=1
                i+=1
            else:
                prev_seq = max(prev_seq,seq)
                i=j
                seq = 1
        return(max(prev_seq,seq))
            
                
        