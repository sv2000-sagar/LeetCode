"""Time: O(E⋅α(n)), where E is the number of edges.
The find function uses path compression, reducing the amortized time complexity
of each find operation to O(α(n)), where α(n) is the inverse Ackermann function."""

#Union Find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(x):
            if(x != parent[x]):
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            uRoot, vRoot = find(u), find(v)
            if(uRoot == vRoot):
                return False
            if(rank[uRoot] > rank[vRoot]):
                parent[vRoot] = uRoot
                rank[uRoot] +=1
            else:
                parent[uRoot] = vRoot
                rank[vRoot] +=1
            return
        
        for u,v in edges:
            if(union(u,v) == False):
                return [u,v]