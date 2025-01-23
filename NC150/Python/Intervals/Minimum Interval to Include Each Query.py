# Time: O(NLogN+MLogM)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        resIndex = {}
        minHeap = []
        i = 0
        for q in sorted(queries):
            # Add all intervals that start before or when the query occurs
            while(i < len(intervals) and q >= intervals[i][0]):
                l,r = intervals[i]
                heapq.heappush(minHeap,(r-l+1,r))
                i+=1
             # Remove intervals from heap that cannot cover the query
            while(minHeap and minHeap[0][1] < q):
                heapq.heappop(minHeap)
            resIndex[q] = minHeap[0][0] if minHeap else -1 

        return [resIndex[q] for q in queries]