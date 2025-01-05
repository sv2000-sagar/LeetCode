# Time:O(n+p)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        cycle, visited = set(), set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course) # current DFS path
            for pre in preMap[course]:
                if(dfs(pre) == False):
                    return False
            cycle.remove(course)
            visited.add(course) # fully procecessed i.e met all prereq
            res.append(course)
            return True
        
        for course in range(numCourses):
            if(dfs(course) == False):
                return []
        return res