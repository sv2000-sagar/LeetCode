# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        l,r = 0,1 #l-buy r-sell
        while(r < len(prices)):
            profit = prices[r] - prices[l]
            maxPro = max(maxPro,profit)
            if(prices[l]>prices[r]): l=r
            r+=1
        return maxPro

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = 0
#         maxProfit = 0
#         for r in range(len(prices)):
#             profit = prices[r] - prices[l]
#             maxProfit = max(maxProfit,profit)
#             if(prices[r] < prices[l]):
#                 l=r
#         return maxProfit      