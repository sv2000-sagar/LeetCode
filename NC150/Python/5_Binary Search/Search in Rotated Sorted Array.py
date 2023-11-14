# Time: O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] == target): return mid

            # left sorted part
            if(nums[l] <= nums[mid]):
                if(target > nums[mid] or target < nums[l]): 
                    l = mid+1 #search right
                else:
                    r = mid-1

            # right sorted part
            else:
                if(target < nums[mid] or target > nums[r]):
                    r = mid-1 #search left
                else:
                    l = mid+1 
        return -1