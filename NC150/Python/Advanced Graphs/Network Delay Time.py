# Dijkstra's Algorithm
# Time: O(E.logV)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        minHeap = [(0, k)]  # (time to reach node, node)
        shortest_dist = {}
        while minHeap:
            cur_t, u = heapq.heappop(minHeap)
            
            if u in shortest_dist:
                continue
            
            # Record the shortest time to reach this node
            shortest_dist[u] = cur_t
            
            # Explore neighbors
            for neighbor, weight in adj[u]:
                if neighbor not in shortest_dist:
                    heapq.heappush(minHeap, (cur_t + weight, neighbor))
        
        # If all nodes are reached, return the maximum time
        if len(shortest_dist) == n:
            return max(shortest_dist.values())
        else:
            return -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        dist_found = set()
        t = 0
        minHeap = [[0,k]]
        for u,v,w in times:
            adj[u].append([v,w])
        while(minHeap):
            w1,node = heapq.heappop(minHeap)
            if(node in dist_found):
                continue
            t = max(t,w1)
            dist_found.add(node)
            for nei,w2 in adj[node]:
                if(nei not in dist_found):
                    heapq.heappush(minHeap,[w1+w2,nei])
        return t if(len(dist_found) == n) else -1