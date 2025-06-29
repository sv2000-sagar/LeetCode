# Time: O(n*m)
# Space: O(n*m)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        oldC = image[sr][sc]
        if oldC == color:
            return image  # Prevents infinite loop
        def dfs(r,c):
            if(r < 0 or r >= rows or
               c < 0 or c >= cols or
               image[r][c] != oldC):
               return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        dfs(sr,sc)
        return image