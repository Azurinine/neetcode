# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return
            l, r = node.left, node.right
            node.right = l
            node.left = r

            helper(l)
            helper(r)
        
        helper(root)
        return root
        