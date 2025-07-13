# Time: O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            v1 = nums[i]
            l,r = i+1, len(nums)-1
            while(l < r):
                total = v1 + nums[l] + nums[r]
                if(total > 0):
                    r -= 1
                elif(total < 0):
                    l += 1
                else:
                    res.append([v1,nums[l],nums[r]])
                    l += 1
                    r-=1
                    while(nums[l] == nums [l-1] and l < r):
                        l+=1
        return res