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
            # checking if pattern has only * left
            if(i == len(s) and j < len(p)):
                for c in p[j:]:
                    if(c != "*"):
                        return False
                return True
            # match
            if(s[i] == p[j] or p[j] == "?"):
                return dfs(i+1,j+1)
            if(p[j] == "*"):
                use = dfs(i+1,j) # * use
                skip = dfs(i,j+1) # not used
                return use or skip
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
            # checking if pattern has only * left
            if(i == len(s) and j < len(p)):
                for c in p[j:]:
                    if(c != "*"):
                        return False
                return True
            if(cache[i][j] != None):
                return cache[i][j]
            # match
            if(s[i] == p[j] or p[j] == "?"):
                cache[i][j] = dfs(i+1,j+1)
                return cache[i][j]
            if(p[j] == "*"):
                use = dfs(i+1,j) # * use
                skip = dfs(i,j+1) # not used
                cache[i][j] = use or skip
                return cache[i][j]
            cache[i][j] = False
            return cache[i][j]
        return dfs(0,0)     