# Time: O(nlogn)
# Space: O(n)
class Solution:
    def maxMeetings(self, start, end):
        arr = list(zip(start,end))
        arr.sort(key = lambda x: x[1]) # sorted based on their end times
        prevEndTime = arr[0][1]
        count = 1
        for i in range(1,len(arr)):
            startTime,endTime = arr[i]
            if(startTime > prevEndTime):
                count += 1
                prevEndTime = endTime
        return count