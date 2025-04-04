class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if(numRows < 2):
            return ans[:numRows]
        for i in range(2,numRows):
            temp = ans[-1]
            res = [1]
            for i in range(len(temp)-1):
                res.append(temp[i] + temp[i+1])
            res.append(1)
            ans.append(res)
        return ans