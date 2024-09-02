class MedianFinder:

    def __init__(self):
         # two heaps, large, small, minheap, maxheap
        self.smallHeap, self.largeHeap = [],[]
        
    # Time: O(logn)
    def addNum(self, num: int) -> None:
        # small nums in left (LargeHeap)
        # big nums in right (small Heap)
        if(self.smallHeap and num > self.smallHeap[0]):
            heapq.heappush(self.smallHeap,num)
        else:
            heapq.heappush(self.largeHeap,-num)

        # uneven size
        if(len(self.largeHeap) > len(self.smallHeap) + 1):
            val = -(heapq.heappop(self.largeHeap))
            heapq.heappush(self.smallHeap,val)
        if(len(self.smallHeap) > len(self.largeHeap) + 1):
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap,-val)

    # Time: O(1)
    def findMedian(self) -> float:
        if(len(self.smallHeap) > len(self.largeHeap)):
            return self.smallHeap[0]
        if(len(self.largeHeap) > len(self.smallHeap)):
            return -(self.largeHeap[0]) 
        return (self.smallHeap[0] + (-self.largeHeap[0])) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()