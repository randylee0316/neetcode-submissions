# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(1, head)
        first= dum
        second=  head
        for i in range(n):
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dum.next
        
        