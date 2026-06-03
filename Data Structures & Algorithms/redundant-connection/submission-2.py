class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        l = [[] for _ in range(n+1)]
        for i, j in edges:
            l[i].append(j)
            l[j].append(i)

        def dfs(start, curr, prev, s):
            if len(s) != 0 and curr == start:
                return (True, s)
            if curr in s:
                return (False, 0)
            s.add(curr)
            for i in l[curr]:
                if i != curr and i != prev:
                    r = dfs(start, i, curr, s)
                    if r[0]:
                        return (True, r[1])
            s.remove(curr)
            return (False, 0)

        for i in range(1, n+1):
            res = dfs(i, i, -1, set())
            if res[0]:
                x = res[1]
                break
        for u, v in reversed(edges):
            if u in x and v in x:
                return [u, v]
        

        



            
            







