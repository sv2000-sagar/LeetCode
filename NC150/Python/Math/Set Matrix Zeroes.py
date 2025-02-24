# Time: O(m*n)
# Space: O(1) In-Place
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        firstRow = False

        # Determine if first row or first column needs to be zeroed
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    if(i != 0):
                        matrix[i][0] = 0
                    else:
                        firstRow = True

        # Zero out marked rows and columns
        for r in range(1,rows):
            for c in range(1,cols):
                if(matrix[0][c] == 0 or matrix[r][0] == 0):
                    matrix[r][c] = 0

        # Handle first column separately
        if(matrix[0][0] == 0):
            for r in range(rows):
                matrix[r][0] = 0
        # Handle first row separately
        if(firstRow == True):
            for c in range(cols):
                matrix[0][c] = 0

# Time: O(m*n)
# Space: O(n+m)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setRows, setCols = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == 0):
                    setRows.add(i)
                    setCols.add(j)
        for r in setRows:
            for c in range(cols):
                matrix[r][c] = 0
        for c in setCols:
            for r in range(rows):
                matrix[r][c] = 0