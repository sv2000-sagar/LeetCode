# Time: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def prevSmaller():
            resSmaller = [-1]*len(heights)
            stack = [] # (i,val)
            for i in range(len(heights)-1,-1,-1):
                while(stack and stack[-1][1] > heights[i]):
                    resSmaller[stack.pop()[0]] = i
                stack.append((i,heights[i]))
            return resSmaller

        def nextSmaller():
            resSmaller = [len(heights)]*len(heights)
            stack = [] # (i,val)
            for i in range(len(heights)):
                while(stack and stack[-1][1] > heights[i]):
                    resSmaller[stack.pop()[0]] = i
                stack.append((i,heights[i]))
            return resSmaller

        pSmaller = prevSmaller()
        nSmaller = nextSmaller()
        maxArea = 0

        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (nSmaller[i] - pSmaller[i] - 1))
        return maxArea