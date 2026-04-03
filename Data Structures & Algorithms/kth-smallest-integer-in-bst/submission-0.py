# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = []
        def search(node):
            if not node:
                return
            search(node.left)
            val.append(node.val)
            search(node.right)
        
        search(root)
        return val[k - 1]
            

            
            
            
