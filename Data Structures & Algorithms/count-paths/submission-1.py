class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr1 = [1]*n
        for i in range(1, m):
            arr2 = [1]
            for j in range(1, n):
                arr2.append(arr2[j-1] + arr1[j])
            arr1 = arr2
        return arr1[-1]