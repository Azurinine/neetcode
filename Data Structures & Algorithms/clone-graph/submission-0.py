"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        nodes = {}
        st = [node]
        res = None
        while st:
            cur = st.pop()
            if cur.val not in nodes:
                res = Node(cur.val)
                nodes[cur.val] = res
            node = nodes[cur.val]

            for n in cur.neighbors:
                if n.val not in nodes:
                    nodes[n.val] = Node(n.val)
                    st.append(n)
                node.neighbors.append(nodes[n.val])
        
        return res

            


        