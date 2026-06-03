class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        l = [[] for _ in range(n)]
        for i, j in edges:
            l[i].append(j)
            l[j].append(i)
        
        visited = set()

        def bfs(i):
            if i in visited:
                return False

            q = deque([i])
            prev = -1
            visits = set()
            while q: 
                node = q.popleft()
                visited.add(node)
                if node in visits:
                    continue
                visits.add(node)
                for a in l[node]:
                    if a != node and a != prev:
                        q.append(a)
                prev = node
            
            return True
        count = 0
        for edge in range(n):
            if bfs(edge):
                count += 1
        return count 
        




