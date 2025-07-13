# Time: O(n log n + n * d) d = maxDL
# Space: O(maxDL)

class Solution:
    def JobScheduling(self, Jobs):
      Jobs.sort(key = lambda x: x[2], reverse = True)
      maxDL = 0
      for j in Jobs:
        maxDL = max(maxDL,j[1])
      count,totalProfit = 0,0
      arr = [-1] * (maxDL+1)
      for j in Jobs:
        idd,dl,pro = j
        for i in range(dl,0,-1):
          if(arr[i] == -1):
            arr[i] = pro
            totalProfit += pro
            count +=1
            break
      return [count,totalProfit]