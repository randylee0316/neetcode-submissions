class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        x = True
        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a == ".":
                    continue
                if a in rows[i] or a in columns[j] or a in squares[i//3, j//3]:
                    x = False
                rows[i].add(a)
                columns[j].add(a)
                squares[i//3, j//3].add(a)
        return x



                

        