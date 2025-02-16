# Recursion
# Time: O(m∗n∗4^m∗n)
# Space: O(m*n) Recusrion Stack
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r,c,preVal):
            if(r < 0 or c < 0 or
               r >= rows or c >= cols or
               preVal >= matrix[r][c]):
               return 0
            # pick
            left = dfs(r,c-1,matrix[r][c])
            right = dfs(r,c+1,matrix[r][c])
            top = dfs(r-1,c,matrix[r][c])
            bottom = dfs(r+1,c,matrix[r][c])
            return 1 + max(left,right,top,bottom)
        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r,c,0))
        return longest 

# Top Down
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r,c,preVal):
            if(r < 0 or c < 0 or
               r >= rows or c >= cols or
               preVal >= matrix[r][c]):
               return 0
            if((r,c) in cache):
                return cache[(r,c)]
            # pick
            left = dfs(r,c-1,matrix[r][c])
            right = dfs(r,c+1,matrix[r][c])
            top = dfs(r-1,c,matrix[r][c])
            bottom = dfs(r+1,c,matrix[r][c])
            cache[(r,c)] = 1 + max(left,right,top,bottom)
            return cache[(r,c)]
        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r,c,-1))
        return longest 