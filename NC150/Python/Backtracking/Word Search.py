#Time: O(n*m*4^w)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        path = set()

        def dfs(i,r,c):
            if(i == len(word)): return True # word is complete
            if(r<0 or c<0 or
                r>=rows or c>=cols or # out of bounds
                word[i] != board[r][c] or #char is not in board current pos
                (r,c) in path): # already checked
                return False
                
            path.add((r,c))
            res = (dfs(i+1,r,c+1) or
                   dfs(i+1,r,c-1) or
                   dfs(i+1,r+1,c) or
                   dfs(i+1,r-1,c))
            path.remove((r,c))
            return res

        for i in range(rows):
            for j in range(cols):
                if(dfs(0,i,j)): return True
        return False