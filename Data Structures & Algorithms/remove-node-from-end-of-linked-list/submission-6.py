# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(None, head)
        if not head.next:
            return None
        second = dum
        first = head
        prev = dum
        for i in range(n+1):
            second = second.next
        while second:
            prev = first
            first = first.next
            second = second.next
        prev.next = first.next
        first.next = None
        return dum.next
        
        