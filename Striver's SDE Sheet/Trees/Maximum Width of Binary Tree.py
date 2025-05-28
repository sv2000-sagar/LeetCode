# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            q = deque()
            if root:
                q.append((root, 0))  # (node, index)
            ans = 0
            while q:
                size = len(q)
                minn = q[0][1]  # Normalize to avoid overflow
                first = last = 0
                for i in range(size):
                    node, curIdx = q.popleft()
                    curIdx -= minn
                    if i == 0:
                        first = curIdx
                    if i == size - 1:
                        last = curIdx
                    if node.left:
                        q.append((node.left, curIdx * 2 + 1))
                    if node.right:
                        q.append((node.right, curIdx * 2 + 2))
                ans = max(ans, last - first + 1)
            return ans

        return bfs(root)