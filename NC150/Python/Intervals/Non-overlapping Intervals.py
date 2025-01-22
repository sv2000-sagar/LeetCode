class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for first,last in intervals[1:]:
            if(first < prevEnd):
                res+=1
                prevEnd = min(prevEnd,last)
            else:
                prevEnd = last
        return res  