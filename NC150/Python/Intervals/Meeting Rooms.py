"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        if(len(intervals) > 0):
            prevEnd = intervals[0].end
        else:
            prevEnd = 0
        for i in intervals[1:]:
            if(prevEnd > i.start):
                return False
            else:
                prevEnd = i.end
        return True