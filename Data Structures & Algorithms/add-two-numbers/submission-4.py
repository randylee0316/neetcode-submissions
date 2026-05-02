# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = f = ListNode(0)
        r = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0  
            if val1 + val2 + r > 9:
                prev = (val1 + val2 + r)%10
                r = (val1 + val2 + r)//10
                p = ListNode(prev)
            else:
                p = c = ListNode(val1 + val2+r)
            dummy.next = p
            dummy = p
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not val1 + val2 + r > 9:
                r = 0
        if r != 0:
            dummy.next = ListNode(r)
        return f.next
