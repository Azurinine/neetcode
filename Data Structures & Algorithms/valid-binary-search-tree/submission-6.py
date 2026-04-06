# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = float('-inf')
        isValid = True

        def dfs(node):
            nonlocal isValid
            nonlocal last
            if not node:
                return
            dfs(node.left)
            if not isValid or not node:
                return
            isValid = last < node.val
            last = node.val
            dfs(node.right)
        dfs(root)
        return isValid