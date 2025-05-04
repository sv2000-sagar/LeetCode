def NthRoot(n: int, m: int) -> int:
    l,h = 1, m
    while(l <= h):
        mid = (l+h)//2
        res = mid ** n
        if(res > m):
            h = mid-1
        elif(res < m):
            l = mid + 1
        else:
            return mid
    return -1
