# Time: O(n)
# Space: O(n)
from collections import defaultdict
class Solution:
    def subarraysWithXorK(self, nums, k):
        prefixMap = defaultdict(int)
        count = 0
        xR = 0
        for i in range(len(nums)):
            xR ^= nums[i]
            if((xR == k)):
                count+=1
            if((xR ^ k) in prefixMap):
                count += prefixMap[xR^k]
            prefixMap[xR] +=1
        return count