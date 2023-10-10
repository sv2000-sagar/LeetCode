# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val:index
        for i,val in enumerate(nums):
            diff = target-val
            if(diff in prevMap): return [prevMap[diff],i]
            prevMap[val] = i