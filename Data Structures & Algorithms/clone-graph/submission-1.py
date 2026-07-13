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
            
        nMap = {}
        def dfs(node):
            nonlocal nMap
            if node.val in nMap:
                return nMap[node.val]

            copy = Node(node.val)
            nMap[node.val] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)
            

            


        