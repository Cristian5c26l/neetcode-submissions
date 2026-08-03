class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Optimal Solution
        # Time Complexity: O(log(m * n))
        # Space Complexity: O(1)

        m = len(matrix) - 1 # rows
        #n = len(matrix[0]) # columns
        
        # O(log(m *n)) = O(logm + logn)
        # O(logm)
        L, R = 0, m
        row = None
        while L <= R:
            mid = (L + R) // 2

            if target > matrix[mid][-1]:
                L = mid + 1
            elif target < matrix[mid][0]:
                R = mid - 1
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                break
            else:
                return False
                
        if row is None:
            return False

        # O(logn)
        L, R = 0, len(row) - 1
        while L <= R:
            mid = (L + R) // 2

            if target > row[mid]:
                L = mid + 1
            elif target < row[mid]:
                R = mid - 1
            else:
                return True

        return False