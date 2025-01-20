# Time: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin,leftMax = 0,0
        for c in s:
            if(c == "("): # +1
                leftMin,leftMax = leftMin+1, leftMax+1
            elif(c == ")"): # -1
                leftMin,leftMax = leftMin-1, leftMax-1
            else: # *
                leftMin,leftMax = leftMin-1, leftMax+1
            if(leftMax < 0):
                return False
            if(leftMin < 0):
                leftMin = 0
        return True if leftMin == 0 else False