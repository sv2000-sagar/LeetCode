# Time: O(H)
# Space: O(1)

def predecessorSuccessor(root, key):
    def succ(node):
        s = -1
        while(node):
            if(key >= node.data):
                node = node.right
            else:
                s = node.data
                node = node.left
        return s

    def pre(node):
        p = -1
        while(node):
            if(key <= node.data):
                node = node.left
            else:
                p = node.data
                node = node.right
        return p

    return [pre(root),succ(root)]