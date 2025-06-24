def floorInBST(root, X):
    floor = -1
    while(root):
        if(X >= root.data):
            floor = root.data
            root = root.right
        else:
            root = root.left
    return floor

def findCeil(root, x):
    ceil = -1
    while(root):
        if(x > root.data):
            root = root.right
        elif(x <= root.data):
            ceil = root.data
            root = root.left
    return ceil