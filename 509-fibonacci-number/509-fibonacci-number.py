class Solution:
    def helper(self,n)->int:
        if n==0: return 0
        if n==1: return 1
        return self.helper(n-1)+self.helper(n-2)
    def fib(self, n: int) -> int:
        return(self.helper(n))
        