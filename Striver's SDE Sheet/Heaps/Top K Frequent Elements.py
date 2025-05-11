class Solution:
    # Time: O(NlogK)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        minHeap = []
        for n in nums:
            count[n] += 1
        for num,freq in count.items():
            heapq.heappush(minHeap,(freq,num))
            if(len(minHeap) > k):
                heapq.heappop(minHeap)
        res = []
        while(k > 0):
            res.append((heapq.heappop(minHeap)[1]))
            k-=1
        return res