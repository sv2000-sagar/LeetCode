# Time: O(logn)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # edge cases
        if(len(nums) == 1):
            return nums[0]
        if(nums[0] != nums[1]):
            return nums[0]
        if(nums[len(nums)-1] != nums[len(nums)-2]):
            return nums[len(nums)-1]
        l,r = 1, len(nums)-2
        while(l <= r):
            mid = (l+r)//2
            # unique ele
            if(nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
                return nums[mid]
            # we are on left side
            elif(mid % 2 == 0 and nums[mid] == nums[mid+1] or
                 mid % 2 != 0 and nums[mid] == nums[mid-1]):
                l = mid+1 # eliminate left
            else:
                r = mid-1