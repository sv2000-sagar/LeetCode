# Top-Down
# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        def dfs(i):
            if(i == n):
                return 1
            if(i > n):
                return 0
            if(cache[i] != -1):
                return cache[i]
            one = dfs(i+1)
            two = dfs(i+2)
            cache[i] = one + two
            return cache[i]
        return dfs(0)

# Bottom-up
# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        cache[n], cache[n-1] = 1, 1
        for i in range(n-2,-1,-1):
            cache[i] = cache[i+1] + cache[i+2]
        return cache[0]

# Space Optimization
# Time: O(n)
# Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev1,prev2 = 1,1
        for i in range(n-2,-1,-1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return prev1