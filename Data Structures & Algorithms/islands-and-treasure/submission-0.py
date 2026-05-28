class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque([(i, j)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            visited = set((i, j))
            curr = 0
            while q:
                for _ in range(len(q)):
                    a, b = q.popleft()
                    if grid[a][b] == 0:
                        return curr
                    for h, v in directions:
                        if a+h in range(rows) and b+v in range(cols) and grid[a+h][b+v] != -1 and (a+h, b+v) not in visited:
                            visited.add((a+h, b+v))
                            q.append((a+h, b+v))


                curr += 1
            return INF
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)


                


        