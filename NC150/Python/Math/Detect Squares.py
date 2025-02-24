# Time: add - O(1), Count - O(n)
# Space: O(n)
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        px,py = point
        res = 0
        for x,y in self.points:
            # if not diagonal
            if(abs(x - px) != abs(y -py) or x == px or y == py):
                continue
            if((x,py) in self.points and (px,y) in self.points):
                res += self.points[x,y] * self.points[x,py] * self.points[px,y]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)