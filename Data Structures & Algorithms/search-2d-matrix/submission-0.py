class Solution:
    def search(self, l: int, r: int, matrix: List[List[int]], target: int) -> bool:
        if l > r:
            return False
        m = l + (r - l) // 2

        if target in matrix[m]:
            return True
        if matrix[m][len(matrix[m])-1] < target:
            return self.search(m + 1, r, matrix, target)
        return self.search(l, m - 1, matrix, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search(0, len(matrix)-1, matrix, target)