# Time: O(n! * n^2)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if(len(nums) == 0):
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1): # number can be added at end
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res

#love/striver
#Time: n! * n
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            if(i==len(nums)):
                res.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[i], nums[j] = nums[j], nums[i] # swap
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i] # swap back
        dfs(0)
        return res       