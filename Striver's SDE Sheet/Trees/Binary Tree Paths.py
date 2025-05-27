# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node,arr):
            if(not node):
                return 
            arr.append(str(node.val))
            if(node.left == None and node.right == None):
                res.append(arr.copy())
            dfs(node.left,arr)
            dfs(node.right,arr) 
            arr.pop()
            return False

        dfs(root,[])
        return ["->".join(path) for path in res]