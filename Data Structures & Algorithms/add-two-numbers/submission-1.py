# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, c = ListNode(), False
        res = dummy

        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if c:
                total += 1
            res.next = ListNode(val=total % 10)
            c = total // 10 == 1
            res = res.next
        
        if c:
            res.next = ListNode(1)
        
        return dummy.next