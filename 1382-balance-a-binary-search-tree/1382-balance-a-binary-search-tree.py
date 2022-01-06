# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):
        if not root: return
        self.inorder(root.left,arr)
        arr.append(root)
        self.inorder(root.right,arr)
    def ConstructTree (self,arr,low,high):
        if low >= high: return
        mid = low+(high-low)//2
        root = arr[mid]
        root.left = self.ConstructTree(arr,low,mid)
        root.right = self.ConstructTree(arr,mid+1,high)
        return root
        
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root,arr)
        return(self.ConstructTree(arr,0,len(arr)))
        