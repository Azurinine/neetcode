# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preO, inO):
            if not preO:
                return
            root = TreeNode(preO[0])
            m = inO.index(preO[0])

            root.left = build(preO[1 : m + 1], inO[:m])
            if m + 1 < len(preO):
                root.right = build(preO[m + 1:], inO[m + 1:])
            
            return root

        return build(preorder, inorder)

        #    1 
        #  2    3
        # 4 5  6 7
            
        # 1 2 4 5 3 6 7   -> curr, left, right (pre)
        # 4 2 5 1 6 3 7   -> left, curr, right (ino)
        
        # 2 4 5    3 6 7
        # 4 2 5    6 3 7
        
        # 4   5      6   7
        # 4   5      6   7

