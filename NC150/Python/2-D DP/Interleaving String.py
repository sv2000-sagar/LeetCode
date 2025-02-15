# Recursion
# Time: O(2^m+n)
# Space: O(m+n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1) + len(s2) != len(s3)):
            return False
        def dfs(i,j):
            if(i == len(s1) and j == len(s2)):
                return True
            if(i < len(s1) and s1[i] == s3[i+j]):
                if(dfs(i+1,j)):
                    return True
            if(j < len(s2) and s2[j] == s3[i+j]):
                if(dfs(i,j+1)):
                    return True
            return False
        return dfs(0,0)

# Top Down
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):  
            return False
        cache = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        def dfs(i, j):
            if(i == len(s1) and j == len(s2)):  
                return True
            if(cache[i][j] is not None):  # Memoization check
                return cache[i][j]
            # Check if we can take from s1
            if(i < len(s1) and s1[i] == s3[i + j]):
                if(dfs(i + 1, j)):
                    cache[i][j] = True
                    return cache[i][j]
            # Check if we can take from s2
            if(j < len(s2) and s2[j] == s3[i + j]):
                if(dfs(i, j + 1)):
                    cache[i][j] = True
                    return cache[i][j]
            cache[i][j] = False  # If neither option works
            return cache[i][j]
        return dfs(0, 0)

# Bottom Up
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):  
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if(i < len(s1) and s1[i] == s3[i + j]):
                    if(dp[i+1][j]):
                        dp[i][j] = True
                if(j < len(s2) and s2[j] == s3[i + j]):
                    if(dp[i][j+1]):
                        dp[i][j] = True
        return dp[0][0]