# Time: O(n)
# Space: O(h)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = None
        self.isValid = True
        def inOrder(root):
            if(not root or not self.isValid):
                return 
            inOrder(root.left)
            if(self.pre and self.pre.val >= root.val):
                self.isValid = False
                return
            self.pre = root
            inOrder(root.right)
        inOrder(root)
        return self.isValid