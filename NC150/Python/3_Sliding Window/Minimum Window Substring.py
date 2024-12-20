# Time: O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, countW = {}, {}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        sIndex = 0
        have, need = 0, len(countT)
        l = 0
        length = float("infinity")
        for r in range(len(s)):
            countW[s[r]] = countW.get(s[r],0) + 1
            if(s[r] in countT and countT[s[r]] == countW[s[r]]):
                have += 1
            while(have == need): # shrink window
                if(r-l+1 < length): # new lesser window length
                    length = r-l+1
                    sIndex = l
                countW[s[l]] -=1
                if(s[l] in countT and countW[s[l]] < countT[s[l]]):
                    have -= 1
                l+=1
        return s[sIndex:sIndex+length] if length != float("infinity") else ""