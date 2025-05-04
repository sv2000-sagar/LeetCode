# Striver
# Time: O(n^2)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = []
        fact = 1
        for i in range(1,n):
            num.append(i)
            fact *= i
        num.append(n) # last digit
        k = k -1 # 0-based
        ans = ""
        while(True):
            ans+= str(num[k//fact])
            num.pop(k//fact)
            k = k % fact
            if(not num):
                break
            fact = fact // len(num)
        return ans