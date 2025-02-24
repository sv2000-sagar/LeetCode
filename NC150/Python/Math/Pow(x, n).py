# Striver
# Time: O(logn)
# Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        num = n
        n = abs(n)
        while(n != 0):
            if(n%2 != 0):
                ans *= x
                n -=1
            else:
                x = x*x
                n = n/2
        return ans if num > 0 else 1/ans    