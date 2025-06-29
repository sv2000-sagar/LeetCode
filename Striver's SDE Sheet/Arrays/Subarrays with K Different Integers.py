# two pointers
# Time: O(n)
# Space: O(k)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            countMap = defaultdict(int)
            count = 0
            l,r = 0,0
            for r in range(len(nums)):
                countMap[nums[r]] += 1
                while(len(countMap) > k):
                    countMap[nums[l]] -= 1
                    if(countMap[nums[l]] <= 0):
                        countMap.pop(nums[l])
                    l+=1
                count += r-l+1
            return count
        return helper(k) - helper(k-1)