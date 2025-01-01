# Time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# return max path sum WITHOUT split
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(root):
            if(not root):
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left,0)
            rightMax = max(right,0)
            # compute max path sum WITH split
            self.res = max(self.res,root.val+leftMax+rightMax)
            return root.val + max(leftMax,rightMax)
        dfs(root)
        return self.res