"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set([p,q])
        while p or q:
            if p and p.parent:
                if p.parent in parents: return p.parent
                else: parents.add(p.parent)
                p = p.parent
            if q and q.parent:
                if q.parent in parents: return q.parent
                else: parents.add(q.parent)
                q = q.parent
        
            
        
            
        