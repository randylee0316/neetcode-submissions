class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        lst = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    lst.append((i, j))


        q = deque(lst)
        m = 0
        
        while q:
            for _ in range(len(q)):
                a, b = q.popleft()
                for h, v in directions:
                    if (a+h in range(rows) and b+v in range(cols)
                        and grid[a+h][b+v]==1):
                        grid[a+h][b+v]=2
                        q.append((a+h, b+v))
            m += 1
        
        for i in range(rows):
            if 1 in grid[i]:
                return -1
        return max(m-1, 0)





