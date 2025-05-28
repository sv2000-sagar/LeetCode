# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n)
        # Space: O(h) h = logn (height of tree) avg
        lSet = set()
        res = []
        def traversal(node,level):
            if(not node):
                return None
            if(level not in lSet):
                res.append(node.val)
                lSet.add(level)
            traversal(node.right,level+1)
            traversal(node.left,level+1)
        traversal(root,0)
        return res