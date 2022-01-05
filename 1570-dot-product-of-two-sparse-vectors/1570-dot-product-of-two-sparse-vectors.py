class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparsemap = {}
        for i,n in enumerate(nums):
            if n !=0:
                self.sparsemap[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sm1 = vec.sparsemap
        sm2 = self.sparsemap
        if len(sm1)> len(sm2): 
            min_map = sm2
            max_map  = sm1
        else:
            min_map = sm1
            max_map  = sm2
        res = 0
        for idx in min_map:
            if idx in max_map:
                res += min_map[idx]* max_map[idx]
        return res
                
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)