# Time: O(n*2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,soln):
            if i==len(nums):
                res.append(soln.copy())
                return 
            soln.append(nums[i])
            #picked
            dfs(i+1,soln)
            #not picked
            soln.pop()
            dfs(i+1,soln)
        dfs(0,[])
        return res