# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        area = 0
        while(l<r):
            curArea = min(height[l],height[r]) * (r-l) # have to take lowest height 
            area = max(curArea,area)
            if(height[l]<height[r]): l+=1
            else: r-=1
        return area
        