# Time: O(n*2^n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i,soln,total):
            if(total == target):
                res.append(soln.copy())
                return
            if(i == len(candidates) or total > target):
                return
            soln.append(candidates[i])
            # picked
            dfs(i+1,soln,total + candidates[i])
            # not picked
            soln.pop()
            # skipping next element if it is duplicate
            while(i + 1 < len(candidates) and candidates[i] == candidates[i+1]):
                i+=1
            dfs(i+1,soln,total)
        dfs(0,[],0)
        return res
    

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i,soln,target):
            if(i==len(candidates)):
                if(target == 0):
                    res.append(soln.copy())
                return
            if(candidates[i]<=target):
                soln.append(candidates[i])
                dfs(i+1,soln,target-candidates[i])
                soln.pop()
            while(i+1 < len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            dfs(i+1,soln,target)
        dfs(0,[],target)
        return res