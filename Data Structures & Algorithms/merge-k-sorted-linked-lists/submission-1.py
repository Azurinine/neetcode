# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 

        min_heap = []
        res = ListNode()
        cur = res

        for x in lists:
            if x:
                heapq.heappush(min_heap, NodeWrapper(x))
        
        while min_heap:
            node = heapq.heappop(min_heap).node
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(min_heap, NodeWrapper(node.next))

        return res.next
        