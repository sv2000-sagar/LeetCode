# Time: O(n^2.logn)
# Prim's Algo (Minimum Spanning Tree)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        # calc distance making adj list
        for i in range(len(points)):
            x1,x2 = points[i]
            for j in range(i+1,len(points)):
                y1,y2 = points[j]
                dist = abs(x1-y1) + abs(x2-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        minHeap = [[0,0]]
        visit = set()
        res = 0
        while(len(visit) < len(points)):
            dist, u = heapq.heappop(minHeap)
            if(u in visit):
                continue
            visit.add(u)
            res += dist
            for d,v in adj[u]:
                if(v not in visit):
                    heapq.heappush(minHeap,[d,v])
        return res 