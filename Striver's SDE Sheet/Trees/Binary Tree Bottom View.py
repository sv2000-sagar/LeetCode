from typing import List
from collections import defaultdict,deque

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Time: O(n)
# Space: O(n)
def bottomView(root: BinaryTreeNode) -> List[int]:
    def bfs(root):
        if not root:
            return None
        hashMap = defaultdict(list)
        q = deque([(root,0)]) # (root,vertical idx)
        minV, maxV = 0,0
        while(q):
            node,vIdx = q.popleft()
            minV,maxV = min(minV,vIdx), max(maxV,vIdx)
            hashMap[vIdx].append(node.data)
            if(node.left):
                q.append((node.left,vIdx-1))
            if(node.right):
                q.append((node.right,vIdx+1))
        res = []
        for vI in range(minV,maxV+1):
            res.append(hashMap[vI][-1])
        return res
    return bfs(root)