# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)

        dfs(root)
        for i in range(1, len(tree)):
            if tree[i - 1] >= tree[i]:
                return False
        return True