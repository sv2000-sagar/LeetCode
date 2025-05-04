# Time: O(n log n + n log D) ,  where D = (stalls[-1] – stalls[0]).

def canWePlace(arr,k,dist):
    cowsCount = 1
    lastCow = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] - lastCow >= dist):
            cowsCount +=1
            lastCow = arr[i]
            if(cowsCount == k):
                return True
    return False

def aggressiveCows(stalls, k):
    stalls.sort()
    l,r = 1, stalls[len(stalls)-1] - stalls[0]
    while(l <= r):
        mid = (l+r)//2
        if(canWePlace(stalls,k,mid)):
            l = mid + 1
        else:
            r = mid-1
    return r