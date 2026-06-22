class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        h = len(matrix)
        w = len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        memo = {}
        def dfs(i, j):
            val = matrix[i][j]
            m = 0
            for a, b in directions:
                if i + a >= 0 and i + a < h and j+b >= 0 and j+b < w and matrix[i+a][j+b] > val:
                    if (i+a, j+b) in memo:
                        m = max(m, memo[(i+a, j+b)])
                        continue
                    m = max(m, dfs(i+a, j+b))
            memo[(i, j)] = m+1

            return m + 1
        ma = 0
        for i in range(h):
            for j in range(w):
                ma = max(ma, dfs(i, j))
        return ma

