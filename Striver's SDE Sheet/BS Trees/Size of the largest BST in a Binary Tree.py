
class NodeValue:
    def __init__(self,maxx,minn,maxSize):
        self.maxx = maxx
        self.minn = minn
        self.maxSize = maxSize

def largestBSTSubtree(root):
    # empty tree of BST size 0
    if(not root):
        return NodeValue(float("-inf"),float("inf"),0)

    # postOrder
    left = largestBSTSubtree(root.left)
    right = largestBSTSubtree(root.right)

    # valid BST
    if(left.maxx < root.data and right.minn > root.data):
        return NodeValue(max(right.maxx,root.data),min(left.minn,root.data),(left.maxSize+right.maxSize+1))
    else: # not valid
        return NodeValue(float("inf"),float("-inf"),max(left.maxSize,right.maxSize))

def largestBST(root):
    return largestBSTSubtree(root).maxSize