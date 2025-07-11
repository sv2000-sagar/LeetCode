# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(1) (avg) 
#       O(h) worst
# Space: O(h) 
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        node = self.stack.pop()
        if(node.right):
            cur = node.right
            while(cur):
                self.stack.append(cur)
                cur = cur.left
        return node.val
        
    def hasNext(self) -> bool:
        return True if self.stack else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()