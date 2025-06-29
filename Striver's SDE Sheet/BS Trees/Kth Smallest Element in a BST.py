# Time: O(k) best, O(n) worst
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def inOrder(root):
            if(root == None or self.count >= k):
                return 
            inOrder(root.left)
            self.count+=1
            if(self.count == k):
                self.res = root.val
                return 
            inOrder(root.right)
        inOrder(root)
        return self.res