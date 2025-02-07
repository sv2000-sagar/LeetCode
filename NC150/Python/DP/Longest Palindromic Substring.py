# Time: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0
        for i in range(len(s)):
            # odd
            l,r = i,i
            while(l >=0 and r < len(s) and s[l]==s[r]):
                if(r-l+1 > longest):
                    longest = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
                
            #even
            l = i
            r = i+1
            while(l >=0 and r < len(s) and s[l]==s[r]):
                if(r-l+1 > longest):
                    longest = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res