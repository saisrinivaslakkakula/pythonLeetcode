class Solution:
    def __init__(self, w: List[int]):
        self.cum_s = []
        self.w = w
        cum = 0
        for i,n in enumerate(w):
            cum +=n
            self.cum_s.append(cum)
        b1 = (0,self.cum_s[0])
        self.buckets = []
        self.buckets.append(b1)
        i=1
        while i< len(self.cum_s):
            self.buckets.append((self.buckets[i-1][1],self.cum_s[i]))
            i+=1   
    def pickIndex(self) -> int:
        num = self.cum_s[-1] * random.random()
        for i,sum_v in enumerate(self.cum_s):
            #print(num,bucket)
            if num < sum_v:
                return i
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()