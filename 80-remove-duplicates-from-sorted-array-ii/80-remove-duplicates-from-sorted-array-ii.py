class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=1
        count = 1
        stop_pointer = 0
        while i< len(nums):
            if nums[i] == nums[i-1]: count+=1
            else:
                count = 1
            if count <=2:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j
                
            
                
                
                
        