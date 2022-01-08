'''
x = 4.00
n = 13
O(13)
13//2 => 6
13%2 = 1
pow2 = 4.00 * 4.00
O(log n)
O(1)
'''
class Solution:
    def helper(self,x:float,n:int):
        if n == 0: return 1.0
        half = self.helper(x,n//2)
        if(n%2 ==0): 
            return half*half
        else: 
            return half*half*x
        
    def myPow(self, x: float, n: int) -> float:
        negative = True if n<0 else False
        n = abs(n)
        print(n)
        res = self.helper(x,n)
        print(res)
        return 1/res if negative else res
        
        
        