# Striver
# Time: O(n)
# Space: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        r = 0
        res = [] # i,val
        for r in range(len(nums)):
            if(q and (r-q[0][0]+1) > k): # window len > k
                q.popleft()
            while(q and q[-1][1] <= nums[r]):
                q.pop()
            q.append((r,nums[r]))
            if(r >= k-1): # window has been established
                res.append(q[0][1])
        return res