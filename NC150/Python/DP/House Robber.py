# Maximum Sum of Non-Adjacent Elements


# Top-Down
# Time: O(n)
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums)+1)
        def dfs(i):
            if(i >= len(nums)):
                return 0
            if(cache[i] != -1):
                return cache[i]
            firstH = nums[i] + dfs(i+2) # picked first house
            secondH = dfs(i+1) # not picked first house
            cache[i] = max(firstH,secondH)
            return cache[i]
        return dfs(0)

# Bottom-up
# Time: O(n)
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [0] * n
        cache[n-1] = nums[n-1]
        cache[n-2] = max(nums[n-2], nums[n-1])
        for i in range(n-3,-1,-1):
            cache[i] = max(cache[i+1],(nums[i] + cache[i+2]))
        return cache[0]


# Space Optimization
# Time: O(n)
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f1,f2 = max(nums[n-1],nums[n-2]) , nums[n-1]
        for i in range(n-3,-1,-1):
            cur = max(f1,(nums[i] + f2))
            f2 = f1
            f1 = cur
        return f1