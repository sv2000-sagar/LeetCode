# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = defaultdict(list)
        q = deque([(root,0,0)]) # node,verticalIndex,levelIndex
        while(q):
            node, v, l = q.popleft()
            nodes[v].append((l,node.val))
            if(node.left):
                q.append((node.left,v-1,l+1))
            if(node.right):
                q.append((node.right,v+1,l+1))
        res = []
        for k in sorted(nodes.keys()):
            sorted_values = sorted(nodes[k])
            temp = []
            for l,val in sorted_values:
                temp.append(val)
            res.append(temp)
        return res