class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas) < sum(cost)):
            return -1
        start = 0
        total = 0
        curr = 0
        for i in range(len(gas)):
            if(curr < 0):
                curr = 0
                start = i
            curr += gas[i] - cost[i]
            total = max(total, curr)
        return start