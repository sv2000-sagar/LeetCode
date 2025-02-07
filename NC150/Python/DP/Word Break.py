# Top down
# Time: O(n^2)
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = [None] * (len(s)+1)
        def dfs(i):
            if(i >= len(s)):
                return True
            if(cache[i] != None):
                return cache[i]
            for j in range(i,len(s)):
                if(s[i:j+1] in wordSet):
                    if(dfs(j+1) == True):
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return cache[i]
        return dfs(0)


# Bottom Up
# Time: O(n^2)
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if(s[i:j+1] in wordSet and 
                dp[j+1] == True):
                    dp[i] = True
                    break
        return dp[0]