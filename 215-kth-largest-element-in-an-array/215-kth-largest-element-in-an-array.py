import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        for num in nums: 
            heapq.heappush(l,num)
            if len(l) >k: 
                heapq.heappop(l)
        return l[0]   
    '''
    Idea:
    The idea is, first we add the k elements to the heap and heapify them while adding, we assume these are the last k sorted elements in the list.
    However, the list is not yet complete. whenever k+1th element is added to the heap, our heap, which is already heapified carries no more last k sorted elements but last k+1 sorted elements. 
    to maintain the condition of keeping heap elements to last k sorted, we remove the top element from the heap which is minimum. The heapification then takes place automatically and keeps the condition of heap back to k last sorted elements.
    
    In other words till the point of array traversal, we have last k sorted lements of that sub array
    eg: 
    
    consider array [ 5,16,4,94,1,3,34,2] and consider we have to return last 2nd sorted element of the array.
    during the process of traversing and heapification of array, let's consider our 'i' pointer reached index 4 which is element '1'. 
    we can say that our heap till this point holds last 2 sorted elements of array till that time. which means our heap will have the below values 
      ** [16,94]  **
     
     as we traverse and reach the end, our heap contains values below
        ** [34,94] ** the 2nd largest sorted element ( since k =2) will be the top of the heap.
        suppose if k=3, our final heap will be [16,34,94] in which 3rd last sorted element is 16.
       
    '''


