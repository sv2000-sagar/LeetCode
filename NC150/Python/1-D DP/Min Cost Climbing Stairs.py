# Top-Down
# Time: O(n)
# Space: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost)+1)
        def dfs(i):
            if(i >= len(cost)):
                return 0
            if(cache[i] != -1):
                return cache[i]
            oneJ = dfs(i+1) + cost[i]
            twoJ = dfs(i+2) + cost[i]
            cache[i] = min(oneJ,twoJ)
            return cache[i]
        return min(dfs(0),dfs(1))

# Bottom-up
# Time: O(n)
# Space: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0] * (n+1)
        cache[n-1] = cost[n-1]
        for i in range(n-2,-1,-1):
            cache[i] = min((cost[i]+cache[i+1]), (cost[i]+cache[i+2]))
        return min(cache[0],cache[1])


# Space Optimization
# Time: O(n)
# Space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        f1,f2 = cost[n-2],cost[n-1]
        for i in range(n-3,-1,-1):
            cur = min((cost[i]+f1), (cost[i]+f2))
            f2 = f1
            f1 = cur
        return min(f1,f2)