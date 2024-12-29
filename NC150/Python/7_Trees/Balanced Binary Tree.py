# striver
# Time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsHeight(root):
            if(not root):
                return 0
            lh = dfsHeight(root.left)
            if(lh == -1): return -1 # children were not balanced
            rh = dfsHeight(root.right)
            if(rh == -1): return -1
            if(abs(lh - rh) > 1): # checking if sub tree is balanced
                return -1
            return max(lh,rh) + 1 
        return False if dfsHeight(root) == -1 else True


# Easy approach NC Comment
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):         
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if (abs(left - right) > 1):
                self.balanced= False

            return max(left, right) + 1
        
        dfs(root)       
        return self.balanced