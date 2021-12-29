class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products= [1]
        right_products = [1]
        res = []
        for i in nums:
            
            left_products.append(left_products[len(left_products)-1]*i)
        j= len(nums)-1
        product = 1
        while j>=0:
            right_products.append(nums[j]*right_products[-1])
            j -=1
        print(left_products)
        right_products = right_products[::-1]
        print(right_products)
        for i in range(len(nums)):
            res.append(left_products[i]*right_products[i+1])
        
        return(res)
            
                                
        