class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map_ = Counter(nums)
        for x in map_.values():
            if x>1:return True
        return False
            
        