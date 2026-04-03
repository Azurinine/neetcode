"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_idx = {}
        idx_to_new = []

        idx = 0
        curr = head
        prev = dummy = Node(-1, head, None)
        while curr:
            new = Node(x=curr.val)
            prev.next = new
            prev = new

            idx_to_new.append(new)
            old_to_idx[curr] = idx

            idx += 1
            curr = curr.next

        newCurr = dummy.next
        while head:
            if head.random:
                randIdx = old_to_idx[head.random]
                newCurr.random = idx_to_new[randIdx]
            else:
                newCurr.random = None

            newCurr = newCurr.next
            head = head.next
        
        return dummy.next