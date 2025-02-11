def upperBound(self,arr,x):
        l,r = 0, len(arr)-1
        res = len(arr) 
        while(l<=r):
            mid = (l+r)//2
            if(x <= arr[mid]):
                res = mid
                r = mid-1
            else:
                l = mid + 1
        return res