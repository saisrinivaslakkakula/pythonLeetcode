class Solution:
    def nextGreater(self,nums,i,n):
        min_dif = float('inf')
        min_d_idx = i
        j = i+1
        while j<len(nums):
            if nums[j] > nums[i]:
                #print("CNG:",nums[j])
                if nums[j] - nums[i] < min_dif:
                    min_dif = nums[j] - nums[i]
                    min_d_idx = j
            j+=1
        return min_d_idx
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) ==1: return nums
        #print("-----")
        i=len(nums)-1
        prev = nums[i]
        i-=1
        flag = False
        while i>=0:
            if nums[i] < prev:
                min_dif_idx = self.nextGreater(nums,i,nums[i])
                print("Replace ",nums[i]," with ", nums[min_dif_idx])
                nums[i],nums[min_dif_idx] = nums[min_dif_idx], nums[i]
                print("After replace:", nums)
                print(nums[i+1:])
                nums[i+1:] = sorted(nums[i+1:])
                print(nums)
                flag = True
                break
            else: prev = nums[i]
            i-=1
        if not flag: nums.sort()
        