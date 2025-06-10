# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n)
# Space: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            res = []
            q = deque([root])
            while(q):
                sameLevel = []
                for i in range(len(q)):
                    node = q.popleft()
                    sameLevel.append(node.val)
                    if(node.left):
                        q.append(node.left)
                    if(node.right):
                        q.append(node.right)
                res.append(sameLevel)
                if(len(res) % 2 == 0):
                    res[-1] = res[-1][::-1]
            return res
        return bfs(root)