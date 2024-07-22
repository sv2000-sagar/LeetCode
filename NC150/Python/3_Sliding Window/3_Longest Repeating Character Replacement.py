# Time: O(26.n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChar = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            countChar[s[r]] = 1 + countChar.get(s[r],0)
            if((r-l+1) - max(countChar.values()) > k):
                countChar[s[l]] -= 1
                l+=1
            longest = max(longest,(r-l+1))
        return longest
        