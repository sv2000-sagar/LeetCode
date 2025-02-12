# Recursion
# Time: O(2^n+m)
# Space: O(m+n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        def dfs(i,j):
            if(i == m or j == n):
                return 0
            if(text1[i] == text2[j]):
                return 1 + dfs(i+1,j+1)
            else:
                return max(dfs(i+1,j), dfs(i,j+1)) # max from down and right
        return dfs(0,0)

# Bottom Up
# Time: O(n*m)
# Space: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        cache = [[-1] * (n) for _ in range(m)]
        def dfs(i,j):
            if(i == m or j == n):
                return 0
            if(cache[i][j] != -1):
                return cache[i][j]
            if(text1[i] == text2[j]):
                cache[i][j] = 1 + dfs(i+1,j+1)
                return cache[i][j]
            else:
                cache[i][j] = max(dfs(i+1,j), dfs(i,j+1)) # max from down and right
                return cache[i][j]
        return dfs(0,0)

# Top Down
# Time: O(n*m)
# Space: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(text1[i] == text2[j]):
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]