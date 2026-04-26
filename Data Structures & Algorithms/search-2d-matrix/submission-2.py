class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        l = 0
        r = len(matrix)-1
        while l < r:
            m = (l + r)//2
            if matrix[m][-1] == target:
                return True
            elif matrix[m][-1] < target:
                l = m+1
            else:
                r = m
        a = 0
        b = len(matrix[0])-1
        while a <= b:
            m = (a+b)//2
            if matrix[l][m] == target:
                return True
            elif matrix[l][m] < target:
                a = m + 1
            else:
                b = m-1
        return False
