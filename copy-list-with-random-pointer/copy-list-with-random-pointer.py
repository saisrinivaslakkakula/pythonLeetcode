
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head == None: return None
        curr = head
        add_map = dict()
        while curr:
            newNode = Node(curr.val)
            add_map[curr] = newNode
            curr = curr.next
        curr  = head
        while curr:
            eqcurrent = add_map[curr]
            if curr.next: 
                eqNext = add_map[curr.next]
                eqcurrent.next = eqNext
            if curr.random:
                eqRandom = add_map[curr.random]
                eqcurrent.random = eqRandom
            curr = curr.next
        return add_map[head]
                
                
        
            
        
        