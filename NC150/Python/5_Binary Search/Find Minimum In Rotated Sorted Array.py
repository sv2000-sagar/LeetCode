# Time: O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minNum = float("inf")
        while(l<=r):
            mid = (l+r)//2
            # if entire array is sorted (when you cross point of rotation)
            if(nums[l] <= nums[r]):
                return min(minNum,nums[l])
            elif(nums[l] <= nums[mid]): # left sorted
                minNum = min(minNum,nums[l])
                l = mid+1
            else: # right sorted
                minNum = min(minNum,nums[mid])
                r = mid-1 