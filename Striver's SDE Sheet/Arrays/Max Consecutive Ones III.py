# Striver
# Time: O(n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res= 0
        l = 0
        zeroes = 0
        for r in range(len(nums)):
            if(nums[r] == 0):
                zeroes+=1
            if(zeroes > k):
                if(nums[l] == 0):
                    zeroes -=1
                l+=1
            if(zeroes <= k):
                res = max(res,r-l+1)
        return res