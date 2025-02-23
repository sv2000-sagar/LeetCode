# Floyd's Cycle Detection
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow = 0, 0
        # detect cycle 
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(fast == slow):
                break 
        # finding start of cycle
        slow2 = 0
        while(True):
            slow = nums[slow]
            slow2 = nums[slow2]
            if(slow == slow2):
                return slow