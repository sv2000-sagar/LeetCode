# Recursion
# Time: O(n∗2^n) (Exponential)
# Space: O(n) Recusrion Stack
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        def dfs(i,j):
            if(i > j):
                return 0
            minn = float("inf")
            for k in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + dfs(i,k-1) + dfs(k+1,j)
                minn = min(minn,cost)
            return minn
        return dfs(1,len(cuts)-2)

# Top Down
# Time: O(n^3)
# Space: O(n^2)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        cache = [[-1] * len(cuts) for _ in range(len(cuts))]
        def dfs(i,j):
            if(i > j):
                return 0
            if(cache[i][j] != -1):
                return cache[i][j]
            minn = float("inf")
            for k in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + dfs(i,k-1) + dfs(k+1,j)
                minn = min(minn,cost)
            cache[i][j] = minn
            return cache[i][j]
        return dfs(1,len(cuts)-2)

# Bottom Up
# Time: O(n^3)
# Space: O(n^2)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[0] * len(cuts) for _ in range(len(cuts))]
        for i in range(len(cuts)-2,0,-1):
            for j in range(1,len(cuts)-1):
                minn = float("inf")
                if(i > j): continue
                for k in range(i,j+1):
                    cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                    minn = min(minn,cost)
                dp[i][j] = minn
        return dp[1][len(cuts)-2]