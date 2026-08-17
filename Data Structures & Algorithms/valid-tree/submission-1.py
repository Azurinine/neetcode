class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:
            return False

        visited = [False] * n
        edge = collections.defaultdict(list)
        traveled = set()

        for a, b in edges:
            edge[a].append(b)
            edge[b].append(a)
        
        # graph search
        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            for next_node in edge[node]:
                if (node, next_node) in traveled:
                    continue
                traveled.add((node, next_node))
                traveled.add((next_node, node))
                if not dfs(next_node):
                    return False
            return True
        
        return dfs(0) and all(visited)
                
