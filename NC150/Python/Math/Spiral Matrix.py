# Striver
# Time: O(n*m)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        left, right = 0, cols-1
        ans = []

        while(top <= bottom and left <= right):
            # left to right
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top +=1
            # top to bottom
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -=1
            # right to left
            if(top <= bottom):
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -=1
            # bottom to top
            if(left <= right):
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left +=1
        return ans