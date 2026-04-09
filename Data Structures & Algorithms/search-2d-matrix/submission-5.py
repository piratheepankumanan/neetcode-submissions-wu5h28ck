class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                left = 0
                right = len(matrix[0]) - 1 
                while left <= right:
                    middle = left + (right - left) // 2
                    if matrix[i][middle] == target:
                        return True
                    if matrix[i][middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False            
        return False
