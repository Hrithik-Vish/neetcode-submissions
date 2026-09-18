class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start_row = 0
        end_row = len(matrix) - 1

        while(start_row <= end_row):
            mid_row = start_row + (end_row - start_row) // 2

            if matrix[mid_row][-1] < target:
                start_row = mid_row + 1
            elif matrix[mid_row][0] > target:
                end_row = mid_row - 1
            else:
                break

        if start_row > end_row:
            return False
                
        start = 0
        end = len(matrix[mid_row]) - 1

        while(start <= end):
            mid = start + (end - start) // 2

            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                start = mid + 1
            else: 
                end = mid - 1

        return False
