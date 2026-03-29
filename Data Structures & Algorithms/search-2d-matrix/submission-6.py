class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                return False
            elif matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                low = mid + 1
        return False