# Time: O(n)
# Space: O(k)
def countDistinctElements(arr, k):
    countMap = defaultdict(int)
    l,r = 0,0
    res = []
    for r in range(len(arr)):
        countMap[arr[r]]+=1
        if(r-l+1 >= k):
            res.append(len(countMap))
            countMap[arr[l]]-=1
            if(countMap[arr[l]] <= 0):
                countMap.pop(arr[l])
            l+=1
    return res