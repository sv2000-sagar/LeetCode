# Time: O(n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)): return False
        countS1, countS2 = {}, {}
        matches = 0

        # Intialising Both Dicts
        for c in range(ord('a'),ord('z')+1):
            countS1[chr(c)], countS2[chr(c)] = 0, 0
       # Counting Freq of s1 in both dicts
        for i in range(len(s1)):
            countS1[s1[i]], countS2[s2[i]] = 1 + countS1.get(s1[i],0), 1 + countS2.get(s2[i],0)
        # Checking matches
        for c in range(ord('a'),ord('z')+1):
            matches += (1 if countS1[chr(c)]== countS2[chr(c)] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if(matches == 26): return True

            char = s2[r]
            countS2[char]+=1
            if(countS1[char] == countS2[char]): matches+=1
            elif(countS1[char] + 1 == countS2[char]): matches-=1

            char = s2[l]
            countS2[char]-=1
            if(countS1[char] == countS2[char]): matches+=1
            elif(countS1[char] - 1 == countS2[char]): matches-=1
            
            l+=1
        return matches == 26