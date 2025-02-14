# Recursion
# Time: O(n*a)
# Space: O(n*a) + recursion stack O(a)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i,canBuy):
            if(i >= len(prices)):
                return 0
            if(canBuy):
                buy = dfs(i+1, not canBuy) - prices[i]
                cooldown = dfs(i+1, canBuy)
                return max(buy, cooldown)
            else:
                sell = dfs(i+2, not canBuy) + prices[i]
                cooldown = dfs(i+1, canBuy)
                return max(sell, cooldown)
        return dfs(0, True)

# Top Down
# Time: O(n*a)
# Space: O(n*a) + recursion stack O(a)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i,canBuy):
            if(i >= len(prices)):
                return 0
            if((i,canBuy) in cache):
                return cache[(i,canBuy)]
            if(canBuy):
                buy = dfs(i+1, not canBuy) - prices[i]
                cooldown = dfs(i+1, canBuy)
                cache[(i,canBuy)] = max(buy, cooldown)
                return cache[(i,canBuy)]
            else:
                sell = dfs(i+2, not canBuy) + prices[i]
                cooldown = dfs(i+1, canBuy)
                cache[(i,canBuy)] = max(sell, cooldown)
                return cache[(i,canBuy)]
        return dfs(0, True)  