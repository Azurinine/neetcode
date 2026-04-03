# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0

            lB, lD = dfs(node.left)
            rB, rD = dfs(node.right)
            
            return lB and rB and abs(lD-rD) <= 1, max(lD, rD) + 1
        
        res, _ = dfs(root)
        return res