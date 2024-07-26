# Time: O(n)
# Space: O(n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        fresh, time = 0,0
        q = collections.deque()
        visited = set()

        # couting fresh and adding rottens to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while(q and fresh >0):
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr, c+dc
                    if(
                    row >= 0 and row < rows and
                    col >= 0 and col < cols and
                    grid[row][col] == 1 and
                    (row,col) not in visited
                    ):
                        q.append([row,col])
                        grid[row][col] == 2
                        visited.add((row,col))
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1