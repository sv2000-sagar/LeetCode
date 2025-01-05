# Time: O(V + E)
# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(v):
            if v in visit:
                return
            visit.add(v)
            for j in adj[v]:
                dfs(j)
            return 
        
        res = 0
        for i in range(n):
            if(i not in visit):
                res+=1
                dfs(i)
        return res

# Union Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(u,v):
            uRoot, vRoot = find(u), find(v)
            if(uRoot == vRoot):
                return 0
            if(rank[uRoot] > rank[vRoot]):
                parent[vRoot] = uRoot
                rank[uRoot] += 1
            else:
                parent[uRoot] = vRoot
                rank[vRoot] += 1
            return 1
        
        res = n
        for u,v in edges:
            res -= union(u,v)
        return res