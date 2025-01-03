class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r,c,visited,prevH):
            if(r < 0 or r >= rows or
               c < 0 or c >= cols or
               (r,c) in visited or
               prevH > heights[r][c]):
                return 
            
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        # DFS from first and last row
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])  # Pacific
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # Atlantic

        # DFS from first and last column
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])  # Pacific
            dfs(r, cols - 1, atl, heights[r][cols - 1])  # Atlantic

        return list(atl.intersection(pac))    