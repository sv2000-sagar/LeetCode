# Striver
# Time: O(2^T) 
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,soln,target):
            if(i==len(nums)):
                if(target == 0):
                    res.append(soln.copy())
                return 
            #picked
            if(nums[i]<=target):
                soln.append(nums[i])
                dfs(i,soln, target-nums[i])
                soln.pop()
            #not picked
            dfs(i+1,soln,target)
        dfs(0,[],target)
        return res