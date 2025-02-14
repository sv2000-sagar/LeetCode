# Recursion
# Time: O(2^n)
# Space: O(n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i,total):
            if(i == len(nums)):
                if(total == target):
                    return 1
                return 0
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            return pos+neg
        return dfs(0,0)

# Bottom Up
# Time: O(n * sum(nums)) = O(n*m)
# Space: O(n * m)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i,total):
            if(i == len(nums)):
                if(total == target):
                    return 1
                return 0
            if((i,total) in cache):
                return cache[(i,total)]
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            cache[(i,total)] = pos+neg
            return cache[(i,total)]
        return dfs(0,0)

# Top Down
# Time: O(n * sum(nums)) = O(n*m)
# Space: O(n * m)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1 # 0 elements 0 sum
        # 1 way to sum to 0 with first 0 elements

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]