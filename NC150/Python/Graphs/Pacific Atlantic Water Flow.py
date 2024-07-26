# Time: O(n*m)
# Space: O(n*m)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visited,prevH):
            if(r < 0 or r >= rows or
               c < 0 or c >= cols or
               prevH > heights[r][c] or
               (r,c) in visited):
               return

            visited.add((r,c))
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                adj_r, adj_c = r+dr, c+dc
                dfs(adj_r, adj_c, visited, heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        return pac.intersection(atl)