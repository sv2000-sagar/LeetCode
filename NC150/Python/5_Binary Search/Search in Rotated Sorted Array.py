# Time: O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(target == nums[mid]):
                return mid
            # if left sorted
            elif(nums[l] <= nums[mid]):
                if(nums[l] <= target and nums[mid] >= target):
                    r = mid - 1
                else:
                    l = mid+1 # target is in unsorted part
            # else right will be sorted
            else:
                if(target >= nums[mid] and target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
        return -1      