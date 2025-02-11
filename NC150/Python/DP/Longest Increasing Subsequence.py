# Time: O(n^2)
# Space: O(n^2)
# Top Down
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # prevI coordinate change -1 -> 0
        cache = [[-1] * (n+1) for _ in range(n)]
        def dfs(i,prevI):
            if(i == n):
                return 0
            if(cache[i][prevI+1] != -1):
                return cache[i][prevI+1]
            # pick
            pick = 0
            if(prevI == -1 or nums[prevI] < nums[i]):
                pick = 1 + dfs(i+1,i)
            # not picked
            skip = dfs(i+1,prevI)
            cache[i][prevI+1] = max(pick,skip)
            return cache[i][prevI+1] 
        return dfs(0,-1)

# Bottom Up
# Time: O(n^2)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n,-1,-1):
            for j in range(i+1,n):
                if(nums[i] < nums[j]):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

# Striver
# Most Optimal Soln using Binary Search (Easy too)
# Time: O(logn)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        length = 1
        for i in range(1,len(nums)):
            if(nums[i] > dp[-1]):
                dp.append(nums[i])
                length+=1
            else:
                idx = self.upperBound(dp,nums[i])
                dp[idx] = nums[i]
        return length
        

    def upperBound(self,arr,x):
        l,r = 0, len(arr)-1
        res = len(arr) 
        while(l<=r):
            mid = (l+r)//2
            if(x <= arr[mid]):
                res = mid
                r = mid-1
            else:
                l = mid + 1
        return res