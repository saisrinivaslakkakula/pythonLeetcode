class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx,val in enumerate(nums):
            hash_map[val] = idx
        for i,num in enumerate(nums):
            if (target-num) in hash_map and hash_map[target-num] != i:
                return [i,hash_map[target-num]]
            
        