class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        l = [[] for _ in range(n)]

        for a, b in edges:
            l[a].append(b)
            l[b].append(a)
        visited = set()
        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for j in l[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -2) and len(visited) == n
        

            

