# Time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My soln
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inOrderMap = {}
        for i,val in enumerate(inorder):
            self.inOrderMap[val] = i

        def dfs(preStart, preEnd, inStart, inEnd):
            if(preStart > preEnd or inStart > inEnd):
                return None
            root = TreeNode(preorder[preStart])
            mid = self.inOrderMap[preorder[preStart]]
            leftSize = mid - inStart # how many nodes in left subtree
            root.left = dfs(preStart+1,preStart+leftSize,inStart,mid-1)
            root.right = dfs(preStart + leftSize + 1,preEnd,mid+1,inEnd)
            return root
            
        return dfs(0,len(preorder)-1,0,len(inorder)-1)