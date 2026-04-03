# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node):
            nonlocal res
            if not node:
                return 0
            l_d = helper(node.left)
            r_d = helper(node.right)
            res = max(res, l_d + r_d)
            return max(l_d, r_d) + 1

        helper(root)
        return res

            