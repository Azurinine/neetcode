# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isFound = False
        def dfs(root):
            nonlocal isFound
            if isFound:
                return 
            if not root:
                return
            if root.val == subRoot.val and not isFound:
                isFound = check(root, subRoot)
            dfs(root.left)
            dfs(root.right)
        
        # Return True if subtree
        def check(node, snode):
            if not node or not snode:
                return not node and not snode
            
            if node.val == snode.val:
                return check(node.left, snode.left) and check(node.right, snode.right)
            else:
                return False

        dfs(root)
        return isFound