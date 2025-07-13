# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def dfs(root):
            if(not root):
                return None
            if(root.left):
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
            if(root.right):
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        time = -1
        visited = set()
        q = deque([start])
        visited.add(start)
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    if(nei not in visited):
                        visited.add(nei)
                        q.append(nei)
            time+=1
        return time