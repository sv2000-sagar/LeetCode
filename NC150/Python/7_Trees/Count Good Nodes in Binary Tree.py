# Time: O(n)
# Space: O(n) height of tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# NC
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxVal):
            if(not node):
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal,node.val)
            res += dfs(node.left,maxVal) + dfs(node.right,maxVal)
            return res
        return dfs(root,root.val)
    
# My Solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root,maxVal):
            if(root == None):
                return 
            if(root.val >= maxVal):
                self.res +=1
            maxVal = max(maxVal, root.val)
            dfs(root.left,maxVal)
            dfs(root.right,maxVal) 
        dfs(root,root.val)
        return self.res