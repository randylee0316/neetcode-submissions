class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r,c):
            q = deque([[r, c]])
            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                for h, v in directions:
                    if r + v in range(rows) and c + h in range(cols) and grid[r+v][c+h] == '1' and (r+v, c+h) not in visited:
                        visited.add((r+v, c+h))
                        q.append([r+v, c+h])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands



            


