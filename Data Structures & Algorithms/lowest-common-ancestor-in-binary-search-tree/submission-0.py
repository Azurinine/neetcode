# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        b, s = max(p.val, q.val), min(p.val, q.val)

        def search(node):
            if node.val > b:
                return search(node.left)
            elif node.val < s:
                return search(node.right)
            else:
                return node
        
        return search(root)

        
