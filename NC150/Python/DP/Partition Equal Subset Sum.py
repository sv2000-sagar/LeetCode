# Recursion
# Time: O(2^n)
# Space: O(n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s % 2 != 0):
            return False
        target = s//2
        def dfs(i,total):
            if(total == target):
                return True
            if(total > target or i == len(nums)):
                return False
            # pick
            if(dfs(i+1,total+nums[i]) == True):
                return True
            # not pick
            if(dfs(i+1,total) == True):
                return True
            return False
        return dfs(0,0)

# Top Down
# Time: O(n*target)
# Space: O(n*target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s % 2 != 0):
            return False
        target = s//2
        cache = [[None] * (target+1) for _ in range(len(nums) + 1)]
        def dfs(i,total):
            if(total == target):
                return True
            if(total > target or i == len(nums)):
                return False
            if(cache[i][total] != None):
                return cache[i][total]
            # pick
            pick = dfs(i+1,total+nums[i])
            # not pick
            skip = dfs(i+1,total)
            cache[i][total] = pick or skip
            return cache[i][total]
        return dfs(0,0)

# Bottom Up
# Time: O(n*target)
# Space: O(target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s % 2 != 0):
            return False
        target = s//2
        dp = set()
        dp.add(0) # if last ele is not picked sum can be 0
        for i in range(len(nums)-1,-1,-1):
            newDp = set() # temp set
            for t in dp:
                if(t + nums[i] == target):
                    return True
                newDp.add(t+nums[i])
                newDp.add(t)
            dp = newDp
        return False