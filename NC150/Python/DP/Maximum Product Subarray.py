class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        # if 0 is encountered both will reset to 0
        curMax, curMin = 1,1 
        for n in nums:
            temp = curMax 
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMin * n, temp * n, n)
            res = max(res,curMax)
        return res