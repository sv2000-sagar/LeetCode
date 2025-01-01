# Time: O(n*m)
# Space: O(n*m)

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(not grid):
            return 0 
        rows,cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if(r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] != '1'
            ):
                return 0

            grid[r][c] = '0'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1'):
                    islands+=1
                    dfs(r,c)
        return islands         

# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(not grid):
            return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while(q):
                row,col = q.popleft()
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    adj_r,adj_c = row+dr,col+dc
                    if(adj_r >=0 and adj_r < rows and
                       adj_c >=0 and adj_c < cols and
                       grid[adj_r][adj_c] == "1" and
                       (adj_r,adj_c) not in visited):
                        q.append((adj_r,adj_c))
                        visited.add((adj_r,adj_c))

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    islands+=1
                    bfs(r,c)
                    
        return islands