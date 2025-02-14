# Recursion
# Time: O(3^m*n)
# Space: O(m*n) Recusrion Stack
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        side = 0
        def dfs(r,c):
            if(r < 0 or c < 0 or
               r >= rows or c >= cols or
               matrix[r][c] != "1"):
               return 0
            right = dfs(r,c+1)
            down = dfs(r+1,c)
            diagonal = dfs(r+1,c+1)
            return 1 + min(right,down,diagonal)
        for r in range(rows):
            for c in range(cols):
                if(matrix[r][c] == "1"):
                    side = max(side,dfs(r,c))
        return side * side

# Top Down
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        side = 0
        cache = [[-1] * (cols+1) for _ in range(rows+1)]
        def dfs(r,c):
            if(r < 0 or c < 0 or
               r >= rows or c >= cols or
               matrix[r][c] != "1"):
               cache[r][c] = 0
               return cache[r][c]
            if(cache[r][c] != -1):
                return cache[r][c]
            right = dfs(r,c+1)
            down = dfs(r+1,c)
            diagonal = dfs(r+1,c+1)
            cache[r][c] = 1 + min(right,down,diagonal)
            return cache[r][c]
        for r in range(rows):
            for c in range(cols):
                if(matrix[r][c] == "1"):
                    side = max(side,dfs(r,c))
        return side * side

# Bottom Up
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxSide = 0
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if(matrix[r][c] != "1"):
                    dp[r][c] = 0
                    continue
                right = dp[r][c+1]
                down = dp[r+1][c]
                diagonal = dp[r+1][c+1]
                dp[r][c] = 1 + min(right,down,diagonal)
                maxSide = max(maxSide, dp[r][c])
        return maxSide * maxSide