from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        print(counter)
        for i,c in enumerate(counter):
            if i <k:
                heap.append((counter[c],c))
                heapq.heapify(heap)
                print(heap)
            else:
                if heap[0][0] < counter[c]:
                    heap[0] = (counter[c],c)
                    heapq.heapify(heap)
                    print(heap)
                    
        res = []
        for t in heap:
            res.append(t[1])
        return(res)
            
            
            
                
            
        
        