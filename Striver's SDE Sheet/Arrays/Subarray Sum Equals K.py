class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] = 1 # initial 
        summ,count = 0,0
        for i in range(len(nums)):
            summ += nums[i]
            rem = summ - k
            if(rem in prefixMap):
                count += prefixMap[rem]
            prefixMap[summ] += 1
        return count    