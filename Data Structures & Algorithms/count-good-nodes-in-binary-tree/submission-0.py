# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(cMax, node):
            nonlocal count
            if node:
                cMax = max(node.val, cMax)
                if node.val >= cMax:
                    count += 1
                dfs(cMax, node.left)
                dfs(cMax, node.right)
        
        dfs(root.val, root)
        return count
         