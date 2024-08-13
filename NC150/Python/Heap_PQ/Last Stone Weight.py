# Time: O(nlogn)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones) # O(n) 

        while(len(stones) > 1):
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if(second < first):
                heapq.heappush(stones, -(first-second))
        
        return abs(stones[0]) if stones else 0