class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        i=0
        while i< len(nums):
            if nums[i]!=0:
                nums[idx] = nums[i]
                idx +=1
            i+=1
        j = idx
        while(j< len(nums)):
            nums[j] = 0
            j+=1