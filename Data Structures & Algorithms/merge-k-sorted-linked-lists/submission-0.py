# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.combine(res, lists[i])
        return res

    def combine(self, l1, l2):
        res = ListNode()
        cur = res
        a, b = l1, l2

        while a and b:
            if a.val < b.val:
                cur.next = ListNode(a.val)
                cur = cur.next
                a = a.next
            else:
                cur.next = ListNode(b.val)
                cur = cur.next
                b = b.next
        
        cur.next = a if a else b
        return res.next

        