class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if target == matrix[row][column]:
                    return True
        return False
                