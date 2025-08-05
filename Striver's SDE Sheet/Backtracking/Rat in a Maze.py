# Time: O(4^(m*n))
# Space: O(m*n)
class Solution:
    def findPath(self, grid):
        res = []
        visited = set()
        m,n = len(grid), len(grid[0])
        def dfs(i,j,path):
            if(i < 0 or i >= m or
               j < 0 or j >= n or
               grid[i][j] == 0 or
               (i,j) in visited):
               return
            if(i == m-1 and j == n-1):
                res.append(path)
                return
            visited.add((i,j))
            down = dfs(i+1,j,path+"D")
            left = dfs(i,j-1,path+"L")
            right = dfs(i,j+1,path+"R")
            up = dfs(i-1,j,path+"U")
            visited.remove((i,j))
        if(grid[0][0] == 1):
            dfs(0,0,"")
        return res