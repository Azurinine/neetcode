# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        q.append(root)

        res = []
        while q:
            temp = []
            cLen = len(q)
            for _ in range(cLen):
                pop = q.popleft()
                if pop:
                    temp.append(pop.val)
                    q.append(pop.left)
                    q.append(pop.right)
            if temp:
                res.append(temp)

        return res