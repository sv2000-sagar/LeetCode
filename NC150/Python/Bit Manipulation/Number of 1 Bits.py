class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while(n):
            res += n % 2 # return 1 if bit is 1
            n = n >> 1 # shift 1 bit
        return res