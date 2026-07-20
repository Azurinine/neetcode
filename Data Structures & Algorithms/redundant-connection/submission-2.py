class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # represents n - 1's parent
        parent = [-1] * len(edges)

        def getParent(i):
            if parent[i] == -1:
                return i
            parent[i] = getParent(parent[i])
            return parent[i]

        # for parent, edge in edges:
        for n1, n2 in edges:
            # get parent or both edges
            n1_id = n1 - 1
            n2_id = n2 - 1

            p1 = getParent(n1_id)
            p2 = getParent(n2_id)
            # if same parent return edge
            if p1 == p2:
                return [n1, n2]
            # else update
            else:
                parent[p2] = p1
        return edges[-1]