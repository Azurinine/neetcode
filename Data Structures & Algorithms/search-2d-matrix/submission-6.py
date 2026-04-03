class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1

        row = []
        while (i <= j):           
            mid = (i + j) // 2
            temp = matrix[mid]
            
            left = temp[0]
            right = temp[-1]
            if (left == target):
                return True
            elif (right == target):
                return True
            elif (left < target and target < right):
                row = temp
                break
            elif (left > target):
                j = mid - 1
            else:
                i = mid + 1

        l = 0
        r = len(row) - 1
        print(row)
        while (l <= r):
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False 