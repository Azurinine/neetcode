# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        # Reversing list
        prev = None
        while (slow != None):
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex

        headTurn = True
        while (prev != head):
            if headTurn:
                temp = head.next
                head.next = prev
                head = temp
            else:
                temp = prev.next
                prev.next = head
                prev = temp
            headTurn = not headTurn
    
                
            