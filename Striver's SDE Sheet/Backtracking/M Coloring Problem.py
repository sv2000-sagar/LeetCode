# Time: O(m^n)
# Space: O(n + E)
from collections import defaultdict
class Solution:
    def graphColoring(self, edges, m, n):
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        color = {}
        for node in range(n):
            color[node] = 0

        def isSafe(node,c):
            adjNodes = adj[node]
            for adjN in adjNodes:
                if(color[adjN] == c):
                    return False
            return True

        def dfs(node):
            if(node == n):
                return True
            for j in range(1,m+1):
                if(isSafe(node,j)):
                    color[node] = j
                    if(dfs(node+1)):
                        return True
                    color[node] = 0
            return False

        return dfs(0)