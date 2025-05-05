# Time: O(n * log(sum(arr) - max(arr)))

def countStudents(arr, maxPages):
    studentPages = arr[0]
    student = 1
    for i in range(1,len(arr)):
        if(studentPages + arr[i] <= maxPages):
            studentPages += arr[i]
        else:
            student +=1
            studentPages = arr[i]
    return student

def findPages(arr: [int], n: int, m: int) -> int:
    if(m > n):
        return -1
    l,r = max(arr), sum(arr)
    while(l<=r):
        mid = (l+r)//2
        students = countStudents(arr,mid)
        if(students > m):
            l = mid + 1 # find more pages
        else:
            r = mid-1
    return l
        
