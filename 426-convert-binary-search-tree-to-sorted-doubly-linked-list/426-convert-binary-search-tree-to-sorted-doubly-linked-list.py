"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def helper(self,node,queue):
        if not node: return
        self.helper(node.left,queue)
        queue.append(node)
        self.helper(node.right,queue)
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        if not root.left and not root.right: 
            root.left = root.right = root 
            return root
        queue = deque()
        self.helper(root,queue)
        head = tail = queue.popleft()
        while queue:
            curr = queue.popleft()
            tail.right = curr
            curr.right = head
            curr.left = tail
            tail = curr
            head.left = tail
        return(head)
        