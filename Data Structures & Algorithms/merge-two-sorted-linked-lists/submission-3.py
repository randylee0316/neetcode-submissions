# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
                curr = list1
                next1 = curr.next
                next2 = list2
        else:
            curr = list2
            next1 = list1
            next2 = curr.next
        start = curr
        while next1 and next2:
            if next1.val <= next2.val:
                curr.next = next1
                curr = next1
                next1 = curr.next
            else:
                curr.next = next2
                curr = next2
                next2 = curr.next
        if next1:
            curr.next = next1
        elif next2:
            curr.next = next2
        return start
