# Top-Down
# Time: O(n)
# Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1] * (len(s)+1)
        def dfs(i):
            if(i == len(s)):
                return 1
            if(cache[i] != -1):
                return cache[i]
            if(s[i] == "0"):
                return 0
            res = dfs(i+1) # one Char
            if(i+1 < len(s)):
                if(s[i] == "1" or
                   s[i] == "2" and s[i+1] < "7"):
                    res += dfs(i+2) # two char
            cache[i] = res
            return res
        return dfs(0)

# Bottom-up
# Time: O(n)
# Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(len(s)-1,-1,-1):
            if(s[i] == "0"):
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

                if(i+1 < len(s)):
                    if(s[i] == "1" or
                    s[i] == "2" and s[i+1] < "7"):
                        dp[i] += dp[i+2] # two char
        return dp[0]

# Space Optimization
# Time: O(n)
# Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f1,f2 = 1,0
        for i in range(len(s)-1,-1,-1):
            if(s[i] == "0"):
                cur = 0
            else:
                cur = f1

                if(i+1 < len(s)):
                    if(s[i] == "1" or
                    s[i] == "2" and s[i+1] < "7"):
                        cur += f2 # two char
            f2 = f1
            f1 = cur
        return f1