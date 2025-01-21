class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]] #stack
        for first,last in intervals[1:]:
            prevEnd = res[-1][1]
            if(prevEnd >= first):
                res[-1][1] = max(prevEnd, last)
            else:
                res.append([first,last])
        return res