class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res =[]
        intervals.sort()
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            curr = intervals[i]
            lastInRes = res[-1]
            if curr[0] >= lastInRes[0] and curr[0]<=lastInRes[1]:
                lastInRes[1] = max(curr[1],lastInRes[1])
            else:
                res.append(curr)
        return(res)
        