# Time: O(s+t)
# Space: O(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)): return False
        hashS,hashT = {},{}
        for n in range(0,len(s)):
            hashS[s[n]] = hashS.get(s[n],0) + 1
            hashT[t[n]] = hashT.get(t[n],0) + 1
        return hashS==hashT