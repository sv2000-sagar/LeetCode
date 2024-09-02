# Time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            q = deque()
            if(root):
                q.append(root)
            res = []
            while(q):
                sameLevelNodes = []
                for i in range(len(q)):
                    cur = q.popleft()
                    if(cur.left):
                        q.append(cur.left)
                    if(cur.right):
                        q.append(cur.right)
                    sameLevelNodes.append(cur.val)
                res.append(sameLevelNodes)
            return res
        return bfs(root)
        