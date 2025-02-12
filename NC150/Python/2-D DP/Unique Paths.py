# Recursion
# Time: O(2^n+m)
# Space: O(m+n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            return right + down  
        return dfs(0, 0)

# Bottom Up
# Time: O(n*m)
# Space: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if(cache[i][j] != -1):
                return cache[i][j]
            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            cache[i][j] = right + down 
            return cache[i][j] 
        return dfs(0, 0)

# Top Down
# Time: O(n*m)
# Space: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                right = dp[i][j+1]
                down = dp[i+1][j]
                dp[i][j] += right + down
        return dp[0][0]

# Space Optimized
# Time: O(n*m)
# Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]