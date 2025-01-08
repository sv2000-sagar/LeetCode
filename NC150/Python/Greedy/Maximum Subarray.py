# Kadane's Algo
# Time: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for i in range(len(nums)):
            if(curSum < 0):
                curSum = 0
            curSum+=nums[i]
            maxSum = max(maxSum,curSum)
        return maxSum

# Prints sub-array using two pointers
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r = 0,0
        maxSum = nums[0]
        curSum = 0
        for r in range(len(nums)):
            if(curSum < 0):
                curSum = 0
                l=r
            curSum += nums[r]
            maxSum = max(maxSum,curSum)
        s = 0
        for i in range(l,len(nums)):
            s+=nums[i]
            print(nums[i])
            if(s==maxSum):
                break
        return maxSum    