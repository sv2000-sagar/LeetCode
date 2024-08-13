# Time: O(klogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        maxHeap = nums
        heapq.heapify(maxHeap)
        while(k > 1):
            heapq.heappop(maxHeap)
            k-=1
        return -(maxHeap[0])