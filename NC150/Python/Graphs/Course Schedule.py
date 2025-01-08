# Time: O(n+p)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        visited = set()
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(course):
            if(course in visited):
                return False
            if(preMap[course] == []):
                return True

            visited.add(course)
            for pre in preMap[course]:
                if (not dfs(pre)):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if(not dfs(course)): return False
        return True
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        cycle, visited = set(), set()
        res = []

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if(crs in visited):
                return True
            if(crs in cycle):
                return False
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if(dfs(pre) == False):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if(dfs(i) == False):
                return False
        return len(res) == numCourses