# Time: O(nlogn)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        res = 0
        r = len(nums)-1
        for l in range(len(nums)):
            while(l <= r and nums[l] + nums[r] > target):
                r -= 1
            if(l <= r):
                res += pow(2,r-l,mod)
                res %= mod
        return res