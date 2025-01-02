# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if(root == None or root == p or root == q):
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if(left == None):
                return right
            elif(right == None):
                return left
            else:
                return root
        return dfs(root)