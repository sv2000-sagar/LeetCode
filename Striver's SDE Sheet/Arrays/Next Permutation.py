# Striver
# Time: O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = -1
        for i in range(len(nums)-1,0,-1):
            if(nums[i] > nums[i-1]):
                idx = i-1
                break
        print(idx)
        # This is the last permutation in order
        if(idx == -1):
            self.reverse(0,len(nums)-1,nums)
        else:
            for i in range(len(nums)-1,idx,-1):
                if(nums[idx] < nums[i]):
                    nums[idx], nums[i] = nums[i], nums[idx]
                    break
            self.reverse(idx+1,len(nums)-1,nums)

    def reverse(self,l,r,nums):
        while(l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1