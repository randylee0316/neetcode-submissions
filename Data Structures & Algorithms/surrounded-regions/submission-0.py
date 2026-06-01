class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        

        def bfs(i, j):
            q = deque([(i, j)])
            visited = set((i, j))
            coords = [(i, j)]
            while q:
                for _ in range(len(q)):
                    a, b = q.popleft()
                    for h, v in directions:
                        if (a+h in range(r) and b+v in range(c) and (a+h, b+v) not in visited and 
                            board[a+h][b+v] == 'O'):
                            visited.add((a+h, b+v))
                            coords.append((a+h, b+v))
                            q.append((a+h, b+v))
            
            if not any(x == 0 or x == r-1 or y == 0 or y == c-1 for x, y in coords):
                for x, y in coords:
                    board[x][y] = 'X'
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    bfs(i, j)



