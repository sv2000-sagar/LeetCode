# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(H)
# Space: O(H) avg, O(n) worst
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        def dfs(bound):
            if(self.i == len(preorder) or preorder[self.i] > bound):
                return None
            newNode = TreeNode(preorder[self.i])
            self.i += 1
            newNode.left = dfs(newNode.val)
            newNode.right = dfs(bound)
            return newNode
        return dfs(float("inf"))