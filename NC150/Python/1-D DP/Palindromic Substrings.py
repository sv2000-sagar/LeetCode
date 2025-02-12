# Time: O(n^2)
# Two Pointers

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.helper(i,i,s) # odd
            res += self.helper(i,i+1,s) # even
        return res


    def helper(self,li,ri,s):
        l,r = li,ri
        res = 0
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l-=1
            r+=1
            res+=1
        return res