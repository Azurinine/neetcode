# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        q = deque()
        q.append(root)
        res = []
        while q:
            temp = []
            for _ in range(len(q)):
                popped = q.popleft()
                if popped:
                    temp.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if temp:
                res.append(temp)

        
        return [x[-1] for x in res]