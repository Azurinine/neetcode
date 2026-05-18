# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        l = self.serialize(root.left)
        r = self.serialize(root.right)

        return str(root.val) + "," + l + "," + r

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 1:
            return TreeNode(int(data)) if data != "N" else None
        
        d = data.split(",")[:-2]
        print(d)
        root = TreeNode(d[0])
        st = [root]

        left = True
        for x in d[1:]:
            print(x)
            if x == "N":
                if not left:
                    st.pop()
                else:
                    left = False
                continue
            node = TreeNode(x)
            if left:
                st[-1].left = node
            else:
                st.pop().right = node
                left = True
            st.append(node)
        
        return root
            


        

