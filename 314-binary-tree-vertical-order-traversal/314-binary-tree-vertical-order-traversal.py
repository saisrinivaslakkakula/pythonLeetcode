# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        levels = defaultdict(list)
        queue.append((0,root))
        while queue:
            curr_level,curr_node = queue.popleft()
            levels[curr_level].append(curr_node.val)
            if curr_node.left:
                queue.append((curr_level-1,curr_node.left))
            if curr_node.right:
                queue.append((curr_level+1,curr_node.right))
        min_idx = min(levels.keys())
        max_idx = max(levels.keys())
        i = min_idx
        res = []
        while i<= max_idx:
            res.append(levels[i])
            i+=1
        return(res)