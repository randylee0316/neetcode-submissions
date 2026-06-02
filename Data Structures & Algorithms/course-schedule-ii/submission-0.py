class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        d = defaultdict(list)
        for i, j in prerequisites:
            d[i].append(j)

        state = [0] * numCourses
        result = []

        def dfs(a):
            if state[a] == 1:
                return False
            if state[a] == 2:
                return True

            state[a] = 1
            for i in d[a]:
                if not dfs(i):
                    return False

            state[a] = 2
            result.append(a)
            return True

        for p in range(numCourses):
            if not dfs(p):
                return []
        return result