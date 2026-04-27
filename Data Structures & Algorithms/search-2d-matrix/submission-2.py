class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # first find row
        l = 0
        r = len(matrix) - 1

        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] == target:
                return True
            
            if (matrix[mid][-1] > target):
                r = mid - 1
            else:
                l = mid + 1
        
        if matrix[mid][-1] < target and mid + 1 < len(matrix):
            rowIdx = mid + 1
        else:
            rowIdx = mid


        search = matrix[rowIdx]
        l = 0
        r = len(search) - 1

        while l <= r:
            mid = (l + r) // 2
            if search[mid] == target:
                return True
            
            if (search[mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return False