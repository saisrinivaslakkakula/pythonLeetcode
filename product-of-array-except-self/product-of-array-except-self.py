class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products= [1]
        right_products = [1]
        j = len(nums)-1
        while j>=0:
            right_products.append(nums[j]*right_products[-1])
            j-=1
        right_products.pop()
        right_products.reverse()
        cumprod = 1
        res = []
        for i,n in enumerate(nums):
            res.append(cumprod*right_products[i])
            cumprod*=n
        return(res)
            
                                
        