# -distance
# (-dist,x,y), (-dist,x,y)
# map [dist] points
# [1,2,3,4,5]
#from collections import heapq
class Solution:
    def dist(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: # On*log(k)
        heap = [(-self.dist(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.dist(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]
        
        
                
            
        
        