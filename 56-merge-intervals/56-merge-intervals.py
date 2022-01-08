class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= res[-1][0] and intervals[i][0] <= res[-1][1]:
                #print("here")
                #res[-1][0] = min(res[-1][0],intervals[i][0])
                res[-1][1] = max(res[-1][-1],intervals[i][1])
            else:
                res.append(intervals[i])
        return(res)