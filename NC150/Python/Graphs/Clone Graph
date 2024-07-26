"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time: O(n)
# Space: O(n)
# Cracking FAANG
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return 
        clones = {}

        def bfs(node):
            q = collections.deque()
            q.append(node)
            clones[node] = Node(node.val)
            while(q):
                curN = q.popleft()
                for nei in curN.neighbors:
                    if(nei not in clones):
                        clones[nei] = Node(nei.val)
                        q.append(nei)
                    clones[curN].neighbors.append(clones[nei])
            return clones[node]

        return bfs(node)