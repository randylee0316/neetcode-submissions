class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = m - 1

        while l <= h:
            mid = (l + h)//2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                h = mid - 1
            else:
                break
        if not(l <= h):
            return False
        mat = matrix[mid]
        a = 0
        b = n-1
        while a <= b:
            mid = (a+b)//2
            if target > mat[mid]:
                a = mid + 1
            elif target < mat[mid]:
                b = mid - 1
            else:
                return True
        return False
                
        