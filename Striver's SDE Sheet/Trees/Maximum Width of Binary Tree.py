# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(n)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root:
                return None
            q = deque([(root,1)])
            res = 0
            while(q):
                levelNodes = []
                for i in range(len(q)):
                    node,num = q.popleft()
                    levelNodes.append(num)
                    if(node.left):
                        q.append([node.left,num*2])
                    if(node.right):
                        q.append([node.right,(num*2)+1])
                res = max(res,levelNodes[-1]-levelNodes[0]+1)
            return res
        return bfs(root)