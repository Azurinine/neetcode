class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])    
        top, bot = 0, ROWS - 1

        while (top <= bot):
            mid = (top + bot) // 2
            if (matrix[mid][0] > target):
                bot = mid - 1
            elif (matrix[mid][-1] < target):
                top = mid + 1
            else:
                break

        if (top > bot):
            return False
        
        left, right = 0, COLS - 1
        row = matrix[(top + bot) // 2]

        while (left <= right):
            mid = (left + right) // 2
            if (row[mid] < target):
                left = mid + 1
            elif (row[mid] > target):
                right = mid - 1
            else:
                return True
        return False