class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        hashSet = set()
        while(True):
            summ = 0
            for n in str(num):
                summ += int(n)**2
            if(summ == 1 ):
                return True
            if summ in hashSet:
                return False
            hashSet.add(summ)
            num = summ