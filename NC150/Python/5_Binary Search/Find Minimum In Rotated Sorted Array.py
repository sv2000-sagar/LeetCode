# Time: O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            # left sorted part
            if(nums[mid] >= nums[l]):
                minimum = min(minimum,nums[l])
                l = mid+1 #search right
            # right sorted part
            else:
                minimum = min(minimum,nums[mid])
                r = mid-1 #search left
        return minimum  