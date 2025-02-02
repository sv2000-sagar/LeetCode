# Time: O(2^T) 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,soln,total):
            if(total == target):
                res.append(soln.copy())
                return
            if(i == len(candidates) or total > target):
                return
            # picked (choosing same no.)
            soln.append(candidates[i])
            dfs(i,soln,total + candidates[i])
            # not picked (choosing another no.)
            soln.pop()
            dfs(i+1,soln,total)
        dfs(0,[],0)
        return res

# Striver
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
    
# my soln
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,soln,total):
            if(total == target):
                res.append(soln.copy())
                return
            if(i == len(candidates) or total > target):
                return
            # picked (choosing same no.)
            total += candidates[i]
            soln.append(candidates[i])
            dfs(i,soln,total)
            # not picked (choosing another no.)
            total -= soln.pop()
            dfs(i+1,soln,total)
        dfs(0,[],0)
        return res