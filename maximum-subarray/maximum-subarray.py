class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        localmax = globalmax = nums[0]
        for i in range (1,len(nums)):
            localmax = max(nums[i],localmax+nums[i])
            if localmax > globalmax: globalmax = localmax
        return(globalmax)
            
        