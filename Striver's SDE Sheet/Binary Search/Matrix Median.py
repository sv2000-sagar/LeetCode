# Time: O(m log n × log (high−low)).

def upperBound(arr, x):
    l, r = 0, len(arr) - 1
    res = len(arr)
    while l <= r:
        mid = (l + r) // 2
        if x < arr[mid]:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def getSmallerEle(matrix, m, n, x):
    count = 0
    for i in range(m):
        count += upperBound(matrix[i], x)
    return count


def median(matrix: [[int]], m: int, n: int) -> int:
    l = matrix[0][0]
    h = matrix[m-1][n - 1]
    for i in range(m):
        l = min(l,matrix[i][0])
        h = max(h,matrix[i][n-1])
    req = (n*m)//2
    while(l <= h):
        mid = (l+h)//2
        smallerEle = getSmallerEle(matrix,m,n,mid)
        if(smallerEle <= req):
            l = mid+1
        else:
            h = mid-1
    return l