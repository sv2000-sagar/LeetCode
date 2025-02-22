# striver
# Time: O(n*m)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # reversing each row of the matrix
        for i,row in enumerate(matrix):
            matrix[i] = row[::-1]