# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((0,root))
        sum_v = 0
        while queue:
            curr_val,curr_node = queue.popleft()
            cur_sum = curr_val*10 + curr_node.val
            if not curr_node.left and not curr_node.right:
                #print(curr_val,curr_node.val)
                sum_v += cur_sum
                #print(sum_v)
            if curr_node.left:
                queue.append((cur_sum,curr_node.left))
            if curr_node.right:
                queue.append((cur_sum,curr_node.right))
        return(sum_v)
            
                
        