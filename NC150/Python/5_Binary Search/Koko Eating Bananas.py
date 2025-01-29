# Striver
# Time: O(nlogn)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while(l<=r):
            mid = (l+r) //2
            hours = self.getTotalHours(piles,mid)
            if(hours > h):
                l = mid+1
            else:
                r = mid-1
        return l

    def getTotalHours(self,piles,k):
        hours = 0
        for p in piles:
            hours+= ceil(float(p) / float(k))
        return hours