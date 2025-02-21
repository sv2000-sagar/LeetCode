# Recursion
# Time: O(2^(m+n))
# Space: O(m+n) Recusrion Stack
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i,j):
            if(i == len(s) and j == len(p)):
                return True
            if(j == len(p)):
                return False
            
            match = ((i < len(s)) and (s[i] == p[j] or p[j] == "."))
            
            if(j+1 < len(p) and p[j+1] == "*"):
                use_star = match and dfs(i+1,j) # can use star only if char matches
                skip_star = dfs(i,j+2)
                return use_star or skip_star
            if(match):
                return dfs(i+1,j+1)
            return False
        return dfs(0,0)

# Top Down
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[None] * (len(p)+1) for _ in range(len(s)+1)]
        def dfs(i,j):
            if(i == len(s) and j == len(p)):
                return True
            if(j == len(p)):
                return False
            if(cache[i][j] != None):
                return cache[i][j]

            match = ((i < len(s)) and (s[i] == p[j] or p[j] == "."))
            if(j+1 < len(p) and p[j+1] == "*"):
                use_star = match and dfs(i+1,j) # can use star only if char matches
                skip_star = dfs(i,j+2)
                cache[i][j] = use_star or skip_star
                return cache[i][j]
            if(match):
                cache[i][j] = dfs(i+1,j+1)
                return cache[i][j]
            cache[i][j] = False
            return cache[i][j]
        return dfs(0,0)