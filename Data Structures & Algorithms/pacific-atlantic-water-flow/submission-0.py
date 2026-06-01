class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = set()
        atlantic = set()


        def dfs(a, b, visited, prev):
            if ((a, b) in visited or a < 0 or b < 0 or a == len(heights) or b == len(heights[0])
                or heights[a][b] < prev):
                return
            visited.add((a, b))
            
            for h, v in directions:
                dfs(a+h, b+v, visited, heights[a][b])

        for c in range(len(heights[0])):
            dfs(0, c, pacific, 0)
            dfs(len(heights) - 1, c, atlantic, 0)

        for r in range(len(heights)):
            dfs(r, 0, pacific, 0)
            dfs(r, len(heights[0]) - 1, atlantic, 0)
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        
        return res

                            
            




        