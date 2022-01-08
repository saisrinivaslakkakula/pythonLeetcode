# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root,None])
        levels = []
        level = []
        while queue:
            curr = queue.popleft()
            if curr == None and queue: 
                queue.append(None)
                levels.append(level)
                del level
                level = []
            else:
                if curr: level.append(curr)
                if curr and curr.left: queue.append(curr.left)
                if curr and curr.right: queue.append(curr.right)
        levels.append(level)
        res = []
        for level in levels:
            res.append(level[-1].val)
        return(res)
        