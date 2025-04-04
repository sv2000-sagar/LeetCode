# Striver
# Longest Subarray with sum K
# Time: O(n)
# Space: O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        summ,maxL = 0,0
        prefixSumMap = {} # sum -> idx
        for i in range(len(nums)):
            if(nums[i] == 0):
                nums[i] = -1
            summ += nums[i]
            if(summ == 0):
                maxL = max(maxL,i+1)
            rem = summ - 0
            if(rem in prefixSumMap):
                maxL = max(maxL,i-prefixSumMap[rem])
            else:
                prefixSumMap[rem] = i # store left most occurence only
        return maxL