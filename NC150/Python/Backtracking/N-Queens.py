# Best soln by neetcode
# Time: O(n!)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDSet = set() # r+c
        negDSet = set() # r-c
        board = [["."]*n for i in range(n)]
        res = []
        
        def dfs(r):
            if(r==n):
                copy = ["".join(row) for row in board]
                res.append(copy)
            for c in range(n):
                if(c in colSet or r+c in posDSet or r-c in negDSet):
                    continue
                colSet.add(c)
                posDSet.add(r+c)
                negDSet.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                board[r][c] = "."
                colSet.remove(c)
                posDSet.remove(r+c)
                negDSet.remove(r-c)
        
        dfs(0)
        return res