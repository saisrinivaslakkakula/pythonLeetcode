class Solution:
    def helper(self,n,memo)->int:
        if n in memo: return memo[n]
        ans = self.helper(n-1,memo)+self.helper(n-2,memo)
        memo[n] = ans
        return ans
    def fib(self, n: int) -> int:
        memo = {0:0,1:1}
        return(self.helper(n,memo))
        