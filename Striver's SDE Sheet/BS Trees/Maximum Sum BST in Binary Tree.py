# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(n)
class NodeValue:
    def __init__(self,maxx,minn,summ):
        self.maxx = maxx
        self.minn = minn
        self.summ = summ

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        def dfs(node):
             # empty tree of BST size 0
            if(not node):
                return NodeValue(float("-inf"),float("inf"),0)
            # postorder
            left = dfs(node.left)
            right = dfs(node.right)
            # valid BST
            if(left.maxx < node.val and right.minn > node.val):
                summ = left.summ + right.summ + node.val
                self.maxSum = max(self.maxSum,summ)
                return NodeValue(max(right.maxx,node.val),min(left.minn,node.val),summ)
            else:
                return NodeValue(float("inf"),float("-inf"),max(left.summ,right.summ))
        dfs(root)
        return self.maxSum           