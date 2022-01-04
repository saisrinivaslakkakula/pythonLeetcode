class Solution:
    def helper(self,houseNum, nums,memo)->int:
        if houseNum >= len(nums): return 0
        if houseNum in memo: return memo[houseNum]
        else:
            stealFromFirstHouse = nums[houseNum]+self.helper(houseNum+2,nums,memo)
            skipFirstHouse = self.helper(houseNum+1,nums,memo)
            ans =  max(stealFromFirstHouse,skipFirstHouse)
            memo[houseNum] = ans
            return ans
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.helper(0,nums,memo)
        