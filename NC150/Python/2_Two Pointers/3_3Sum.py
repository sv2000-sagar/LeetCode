# Time:O(n^2)
# Space:O(1)/O(n) [Depends on sorting algo]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,val in enumerate(nums):
            if(i>0 and val==nums[i-1]):continue
            l,r=i+1,len(nums)-1
            while(l<r):
                curSome = val+nums[l]+nums[r]
                if(curSome>0):r-=1
                elif(curSome<0):l+=1
                else:
                    result.append([val,nums[l],nums[r]])
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):l+=1
        return result