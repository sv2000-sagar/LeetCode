# Striver
# Time: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i=0
        # Find the correct position for the new interval
        while(i < n and intervals[i][1] < newInterval[0]):
            res.append(intervals[i])
            i+=1
        # Merge intervals that overlap with newInterval
        while(i<n and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
        res.append(newInterval)
        # Rest of all the intervals
        while(i<n):
            res.append(intervals[i])
            i+=1
        return res     