# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head:
            left = head
            right = head.next
            while left and right:
                if left.next:
                    left = left.next
                else:
                    return False
                if right.next and right.next.next:
                    right = right.next.next
                else:
                    return False
                if left == right:
                    return True
        
        return False
