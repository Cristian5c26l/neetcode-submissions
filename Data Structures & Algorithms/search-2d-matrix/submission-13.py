class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Optimal Solution
        # Time Complexity: O(log(m * n))
        # Space Complexity: O(1)

        # O(log(m * n)), where m * n are the total elements
        rows = len(matrix)
        cols = len(matrix[0])
        L, R = 0, rows * cols - 1

        while L <= R:
            mid = (L + R) // 2
            
            if target > matrix[mid // cols][mid % cols]:
                L = mid + 1
            elif target < matrix[mid // cols][mid % cols]:
                R = mid - 1
            else:
                return True

        return False