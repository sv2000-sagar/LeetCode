# Top Down
# Time: O(n*a)
# Space: O(n*a) + recursion stack O(a)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [[-1] * amount for _ in range(len(coins))]
        def dfs(i,total):
            if(total == amount):
                return 1
            if(total > amount or i == len(coins)):
                return 0
            if(cache[i][total] != -1):
                return cache[i][total]
            # pick
            pick = dfs(i, total+coins[i])
            # skip
            skip = dfs(i+1,total)
            cache[i][total] = pick + skip
            return cache[i][total]
        return dfs(0,0)


# Bottom Up
# Time: O(n*a)
# Space: O(n*a)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  
        for i in range(1, n + 1):  # Iterating through each coin
            for total in range(amount + 1):  # Iterating through each total
                # Skip current coin (take previous row's value)
                dp[i][total] = dp[i - 1][total]
                # Pick current coin if it doesn’t exceed `total`
                if total >= coins[i - 1]:
                    dp[i][total] += dp[i][total - coins[i - 1]] 
        return dp[n][amount]
