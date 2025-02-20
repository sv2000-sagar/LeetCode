# Recursion
# Time: O(n∗2^n) (Exponential)
# Space: O(n) Recusrion Stack
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        def dfs(i,j):
            if(i > j):
                return 0
            maxx = float("-inf")
            for k in range(i,j+1):
                coins = nums[i-1] * nums[k] * nums[j+1] + dfs(i,k-1) + dfs(k+1,j)
                maxx = max(maxx,coins)
            return maxx
        return dfs(1,len(nums)-2)


# Top Down
# Time: O(n^3)
# Space: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = [[-1] * len(nums) for _ in range(len(nums))]
        def dfs(i,j):
            if(i > j):
                return 0
            if(cache[i][j] != -1):
                return cache[i][j]
            maxx = float("-inf")
            for k in range(i,j+1):
                coins = nums[i-1] * nums[k] * nums[j+1] + dfs(i,k-1) + dfs(k+1,j)
                maxx = max(maxx,coins)
            cache[i][j] = maxx
            return cache[i][j]
        return dfs(1,len(nums)-2)

# Bottom Up
# Time: O(n^3)
# Space: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)-2,0,-1):
            for j in range(1,len(nums)-1):     
                if(i > j):
                    continue
                maxx = float("-inf")
                for k in range(i,j+1):
                    coins = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    maxx = max(maxx,coins)
                dp[i][j] = maxx
        return dp[1][len(nums)-2]