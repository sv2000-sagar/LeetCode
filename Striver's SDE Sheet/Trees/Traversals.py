class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preOrder(root):
            if(not root):
                return None
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right) 
        preOrder(root)
        return res
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inOrder(root):
                if(root == None):
                    return
                inOrder(root.left)
                res.append(root.val)
                inOrder(root.right)
        inOrder(root)
        return res
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postOrder(root):
            if(not root):
                return None
            postOrder(root.left)
            postOrder(root.right) 
            res.append(root.val)
        postOrder(root)
        return res