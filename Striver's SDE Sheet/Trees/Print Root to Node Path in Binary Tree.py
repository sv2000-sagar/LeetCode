def pathInATree(root: TreeNode, x: int) -> List[int]:
    res = []
    def dfs(node,arr):
        if(not node):
            return False
        arr.append(node.data)
        if(node.data == x):
            res.extend(arr)
            return True
        left = dfs(node.left,arr)
        right = dfs(node.right,arr)
        if(left == True or right == True):
            return True
        arr.pop()
        return False
    dfs(root,[])
    return res