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
        if not root:
            return res
        while q:
            qLen = len(q)
            for i in range(qLen):
                popped = q.popleft()
                if i == qLen - 1:
                    res.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

        # [1]
        
        return res