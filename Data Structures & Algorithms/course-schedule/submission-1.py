class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for i, j in prerequisites:
            d[i].append(j)
        
        visited = set()
        
        def dfs(curr):
            if curr in visited:
                return False
            if d.get(curr, 0) == []:
                return True
            visited.add(curr)
            
            for i in d.get(curr, []):
                if not dfs(i):
                    return False
            
            visited.remove(curr)
            return True
            d[curr] = []
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

            
            

        
