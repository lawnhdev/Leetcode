# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        '''
        This is brute force, and it fails due to a TLE
        a = headA
        b = headB
        while a:
            b = headB
            while b:
                if b == a:
                    return b
                b = b.next
            a = a.next
        return None
        '''

        dictA = {}

        a = headA
        b = headB

        while a:
            dictA[a] = a.val
            a = a.next
        
        while b:
            if b in dictA:
                return b
            b = b.next

        return None
