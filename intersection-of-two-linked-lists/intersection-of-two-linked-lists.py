# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        add = set()
        if not headA or not headB: return None         
        while headA:
            add.add(headA)
            headA = headA.next
        while headB:
            if headB in add: return headB
            headB = headB.next
        return None
        
                
        