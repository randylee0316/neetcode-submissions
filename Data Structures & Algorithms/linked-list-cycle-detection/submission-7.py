# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next and head.next.next:
            a = head.next
            b = head.next.next
        else:
            return False
        while a and b:
            if not a.next or not b.next or not b.next.next:
                return False
            elif a == b:
                return True
            a = a.next
            b = b.next.next
        return False


        