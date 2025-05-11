# babbar
# Time: O(n^2)
# Space: O(n)

def insertSorted(stack,ele):
    if(not stack or stack[-1] < ele):
        stack.append(ele)
        return
    temp = stack.pop()
    insertSorted(stack,ele)
    stack.append(temp)
    

def sortStack(stack):
    if(not stack):
        return []
    top = stack.pop()
    sortStack(stack)
    insertSorted(stack,top)