# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return[]
        queue = deque() #S;O(n)
        queue.append((root,0))
        cols = {} #s;0(n)
        max_key = min_key = 0
        while queue: #O(n)
            curr = queue.popleft() #O(1)
            curr_node = curr[0]
            curr_col = curr[1]
            if curr_node.left: queue.append((curr_node.left,curr_col-1)) #O(1)
            if curr_node.right: queue.append((curr_node.right,curr_col+1))
            if not curr_col in cols: cols[curr_col] = [curr_node.val] #O(1)
            else:cols[curr_col].append(curr_node.val) #O(1)
            if curr_col < min_key : min_key = curr_col
            elif curr_col > max_key: max_key = curr_col
        res = [] #S:O(n)
        #sorted_keys = sorted(cols.keys()) #O(n log n)
        i = min_key
        while i<=max_key: #O(n)
            res.append(cols[i]) #O(n)
            i+=1
        return(res)
        
    
        