# Time: O(n)
# Space: O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        end = 0
        res = []
        lastIndex = {} # char -> last Index in str s
        for i,c in enumerate(s):
            lastIndex[c] = i
        for i,c in enumerate(s):
            size+=1
            end = max(end,lastIndex[c])
            if(i == end):
                res.append(size)
                size = 0
        return res       