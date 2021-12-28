class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = dict()
        
        for i,num in enumerate(nums):
            needed = target - num
            if needed not in found:
                found[num] = i
            else:
                res = [found[needed],i]
                return(res)
                
            
            
        