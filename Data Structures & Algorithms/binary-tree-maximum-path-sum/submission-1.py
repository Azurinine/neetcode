# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            lSum = dfs(node.left)
            rSum = dfs(node.right)

            res = max(res, lSum + rSum + node.val)
            return max(lSum + node.val, rSum + node.val, 0)
        
        dfs(root)
        return res
    
    #     2
    # 1      3

    # dfs(2) -> dfs(1), dfs(3)
    # dfs(1) -> res = 2 -> 
            
            