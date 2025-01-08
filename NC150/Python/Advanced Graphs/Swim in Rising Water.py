# Time: O(n^2*logn)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        while(minHeap):
            ele,r,c = heapq.heappop(minHeap)
            if((r,c) in visit):
                continue
            visit.add((r,c))
            if(r == len(grid) - 1 and c == len(grid[0]) - 1):
                return ele
            for dr,dc in directions:
                row,col = r+dr,c+dc
                if(row >= 0 and row < len(grid) and
                   col >= 0 and col < len(grid[0]) and
                   (row,col) not in visit):
                   heapq.heappush(minHeap, [max(ele, grid[row][col]), row, col])