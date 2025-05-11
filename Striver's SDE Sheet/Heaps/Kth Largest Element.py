class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(nlogk)
        minHeap = []
        for n in range(k):
            heapq.heappush(minHeap,nums[n])
        for n in range(k,len(nums)):
            heapq.heappush(minHeap,nums[n])
            if(len(minHeap) > k):
                heapq.heappop(minHeap)
        return minHeap[0]