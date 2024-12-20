# Time: O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, count = {}, {}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        sIndex = 0
        have, need = 0, len(countT)
        l = 0
        length = float("infinity")
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            if(s[r] in countT and countT[s[r]] == count[s[r]]):
                have += 1
            while(have == need): # shrink window
                if(r-l+1 < length):
                    length = r-l+1
                    sIndex = l
                count[s[l]] -=1
                if(s[l] in countT and count[s[l]] < countT[s[l]]):
                    have -= 1
                l+=1
        return s[sIndex:sIndex+length] if length != float("infinity") else ""