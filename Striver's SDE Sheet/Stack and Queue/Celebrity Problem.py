# Time: O(n)
# Space: O(1)
class Solution:
    def celebrity(self, mat):
        # code here
        top,bottom = 0, len(mat)-1
        while(top < bottom):
            if(mat[top][bottom] == 1): # top knows bottom
                top+=1
            elif(mat[bottom][top] == 1): # bottom know top
                bottom-=1
            else: # both doesn't know each other
                top+=1
                bottom-=1
        if(top > bottom):
            return -1 # no celeb found
        if(top == bottom):
            for i in range(len(mat)):
                if(i == top): continue
                if(mat[top][i] == 1 or mat[i][bottom] == 0):
                    return -1
            return top
