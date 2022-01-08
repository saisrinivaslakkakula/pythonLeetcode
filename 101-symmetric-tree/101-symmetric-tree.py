# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self,root1,root2)->bool:
        if not root1 or not root2:
            return root1 == root2
        if root1.val == root2.val and (self.checkSymmetry(root1.left,root2.right) and self.checkSymmetry(root1.right, root2.left)): return True
        else: return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right): return True
        return(self.checkSymmetry(root,root))
        