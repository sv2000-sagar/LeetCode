# Time: O(n)
# Space:O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix,postfix = 1,1
        for i in range(0,len(nums)):
            res[i] = prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*= postfix
            postfix*=nums[i]
        return res