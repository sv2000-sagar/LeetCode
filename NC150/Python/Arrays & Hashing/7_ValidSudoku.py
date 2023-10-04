# Time: O(9^2)
# Space: O(9^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colHash = defaultdict(set)
        rowHash = defaultdict(set)
        sqHash = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if(board[r][c]=='.'):continue
                if(board[r][c] in rowHash[r] or board[r][c] in colHash[c] or board[r][c] in sqHash[r//3,c//3]):
                    return False
                rowHash[r].add(board[r][c])
                colHash[c].add(board[r][c])
                sqHash[r//3,c//3].add(board[r][c])
        return True