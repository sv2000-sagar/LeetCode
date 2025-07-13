# Neetcode
# Time: O(n)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxL,maxR = height[l], height[r]
        res = 0
        while(l<r):
            if(maxL < maxR):
                l+=1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        preMax, suffMax = [0]*len(height), [0]*len(height)
        preMax[0], suffMax[-1] = height[0], height[-1]
        for i in range(1,len(height)):
            preMax[i] = max(preMax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            suffMax[i] = max(suffMax[i+1],height[i])
        res = 0
        for i in range(len(height)):
            r = min(preMax[i],suffMax[i]) - height[i]
            if(r > 0):
                res += r
        return res