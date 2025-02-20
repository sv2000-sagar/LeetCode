# Recursion
# Time: O(2^m)
# Space: O(m) Recusrion Stack
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i,j):
            if(j == len(t)):
                return 1
            if(i == len(s)):
                return 0
            # pick
            pick = 0
            if(s[i] == t[j]):
                pick = dfs(i+1,j+1)
            # not picked
            skip = dfs(i+1,j)
            return pick+skip
        return dfs(0,0)


# Top Down
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = [[-1] * (len(t)+1) for _ in range(len(s)+1)]
        def dfs(i,j):
            if(j == len(t)):
                return 1
            if(i == len(s)):
                return 0
            if(cache[i][j] != -1):
                return cache[i][j]
            # use
            use = 0
            if(s[i] == t[j]):
                use = dfs(i+1,j+1)
            # not used
            skip = dfs(i+1,j)
            cache[i][j] = use+skip
            return cache[i][j]
        return dfs(0,0)

# Bottom Up
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for r in range(len(s)+1):
            dp[r][len(t)] = 1
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                use = 0
                if(s[i] == t[j]):
                    use = dp[i+1][j+1]
                skip = dp[i+1][j]
                dp[i][j] = use+skip
        return dp[0][0]