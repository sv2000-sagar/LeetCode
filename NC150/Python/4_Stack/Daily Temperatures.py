# Time: O(n)
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = [] # [val,index] pair
        for i,val in enumerate(temp):
            while(stack and val > stack[-1][0]):
                stackVal, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([val,i])
        return res