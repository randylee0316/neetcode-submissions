# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if curr1 and curr2:
            if curr1.val < curr2.val:
                x = curr1
                curr1 = curr1.next
            else:
                x = curr2
                curr2 = curr2.next
        else:
            if curr1:
                return curr1
            elif curr2:
                return curr2
            else:
                return None
        z = x
        while curr1 and curr2:
            if curr1.val < curr2.val:
                y = curr1
                curr1 = curr1.next
            else:
                y = curr2
                curr2 = curr2.next
            x.next = y
            x = x.next
        if curr1:
            x.next = curr1
        elif curr2:
            x.next = curr2
        return z

