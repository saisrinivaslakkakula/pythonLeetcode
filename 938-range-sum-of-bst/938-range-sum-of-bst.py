# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,low,high,res)->int:
        if not node: return 0
        self.helper(node.left,low,high,res)
        if node.val>=low and node.val<=high:
            res.append(node.val)
        self.helper(node.right,low,high,res)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        self.helper(root,low,high,res)
        return(sum(res))