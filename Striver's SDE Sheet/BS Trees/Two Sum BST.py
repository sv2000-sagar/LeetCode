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
        self.stack1 = []
        self.stack2 = []
        self._push(root,False)
        self._push(root,True)
            
    def _push(self,node,reverse):
        cur = node
        while(cur):
            if(reverse == False): # increasing
                self.stack1.append(cur)
                cur = cur.left
            else:
                self.stack2.append(cur) # decreasing
                cur = cur.right

    def next(self) -> int:
        node = self.stack1.pop()
        if(node.right):
            self._push(node.right,False)
        return node.val
    
    def before(self) -> int: # Decreasing inorder
        node = self.stack2.pop()
        if(node.left):
            self._push(node.left,True)
        return node.val

# Time: O(n)
# Space: O(h)  
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = BSTIterator(root)
        l,r = s.next(),s.before()
        while(l<r):
            summ = l+r
            if(summ == k):
                return True
            elif(summ > k):
                r = s.before()
            else:
                l = s.next()
        return False