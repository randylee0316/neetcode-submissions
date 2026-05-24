class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        n = len(board)
        m = len(board[0])

        def dfs(i, j, w):
            if w == len(word):
                return True
            if i < 0 or j < 0 or i == n or j == m or word[w] != board[i][j] or board[i][j] == '#':
                return False

            board[i][j] = '#'
            
            res = dfs(i+1, j, w+1) or dfs(i-1, j, w+1) or dfs(i, j+1, w+1) or dfs(i, j-1, w+1)
            board[i][j] = word[w]
            return res      
            

        for a in range(n):
            for b in range(m):
                if dfs(a, b, 0):
                    return True
        return False

            
            
