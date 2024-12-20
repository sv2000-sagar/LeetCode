# Time: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        l = r = 0
        while(r<len(nums)):
            while(q and nums[r]>nums[q[-1]]): q.pop()
            q.append(r)
            if(l > q[0]): q.popleft() # when window gets slided
            if(r+1 >= k): # once window size is established
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res