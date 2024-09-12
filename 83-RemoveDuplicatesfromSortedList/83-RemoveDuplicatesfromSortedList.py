# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''my_set = set()
        temp = head
        tempHead = temp
        while head is not None:
            if head.val not in my_set:
                my_set.add(head.val)
                temp.val = head.val
                temp.next = head.next
            head = head.next
        return tempHead'''

        my_set = set()
        if head:
            my_set.add(head.val)
        temp = head
        while head and head.next:
            while head.next and head.next.val in my_set:
                head.next = head.next.next
            if head.next:
                my_set.add(head.next.val)
            head = head.next

        return temp
