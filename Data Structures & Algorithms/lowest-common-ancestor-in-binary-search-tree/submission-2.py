# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        A, B = max(p.val, q.val), min(p.val, q.val)
        while curr:
            if curr.val < B:
                curr = curr.right
            elif curr.val > A:
                curr = curr.left
            else:
                break
        return curr