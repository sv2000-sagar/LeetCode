# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n)
# Space: O(H) avg, O(n) worst
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):
            if(l > r):
                return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = dfs(l,mid-1)
            node.right = dfs(mid+1,r)
            return node
        return dfs(0,len(nums)-1)
        