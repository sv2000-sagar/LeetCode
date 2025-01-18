# striver
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i in range(len(nums)):
            if(i > maxIndex):
                return False
            fIndex = i + nums[i] # future Index
            maxIndex = max(maxIndex,fIndex)
        return True