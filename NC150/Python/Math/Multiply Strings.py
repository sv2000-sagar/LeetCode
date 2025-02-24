class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(num1 == "0" or num2 == "0"):
            return "0"
        num1,num2 = num1[::-1], num2[::-1]
        # len of n1*n2 can be max len(n1+n2)
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
                res[i+j+1] += res[i+j] // 10 # carry
                res[i+j] = res[i+j] % 10
        res = res[::-1]
        begin = 0 
        # getting index after trailing 0 eg.06
        for i in range(len(res)):
            if(res[i] != 0):
                begin = i
                break
        res = res[begin:]
        res = list(map(str,res))
        return "".join(res)