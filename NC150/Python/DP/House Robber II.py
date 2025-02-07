class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) <= 1): 
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self,nums):
        n = len(nums)
        f1,f2 = max(nums[n-1],nums[n-2]), nums[n-1]
        for i in range(n-3,-1,-1):
            cur = max(nums[i] + f2, f1)
            f2 = f1
            f1 = cur
        return f1    