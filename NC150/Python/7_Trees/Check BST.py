# Anuj
# Time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node,minn,maxx):
            if(not node):
                return True
            if(node.val < minn or node.val > maxx):
                return False
            return (
            isValid(node.left,minn,node.val-1) and
            isValid(node.right,node.val+1,maxx)
            )
        return isValid(root,float("-inf"),float("+inf"))
    
# my soln
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = None
        self.isValid = True
        def inOrder(root):
            if(not root):
                return 
            inOrder(root.left)
            if(self.pre and self.pre.val >= root.val):
                self.isValid = False
                return
            self.pre = root
            inOrder(root.right)
        inOrder(root)
        return self.isValid