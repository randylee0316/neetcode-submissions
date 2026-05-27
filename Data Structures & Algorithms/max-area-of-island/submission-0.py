class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        m = 0

        def bfs(r, c):
            a = 1
            q = deque([(r, c)])
            grid[r][c] = 0

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                for i, j in directions:
                    if r+i in range(rows) and c+j in range(cols) and grid[r+i][c+j] == 1:
                        q.append((r+i, c+j))
                        grid[r+i][c+j] = 0
                        a += 1
            return a


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    m = max(m, bfs(i, j))
        return m


