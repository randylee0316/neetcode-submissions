class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high)//2

            if target in matrix[mid]:
                return True
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        return False
        