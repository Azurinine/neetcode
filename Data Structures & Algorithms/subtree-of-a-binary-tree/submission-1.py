# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found = False
        def dfs(n):
            nonlocal found
            if found or not n: 
                return
            if n.val == subRoot.val:
                found = self.isSame(n, subRoot)
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return found


    def isSame(self, node, sNode):
        if not node and not sNode:
            return True
        if not node or not sNode or node.val != sNode.val:
            return False
        return self.isSame(node.left,sNode.left) and self.isSame(node.right, sNode.right)