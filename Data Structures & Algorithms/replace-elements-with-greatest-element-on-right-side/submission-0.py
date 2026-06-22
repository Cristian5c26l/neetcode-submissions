class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute force solution
        # Time Complexity: O(n*n)
        # Space Complexity: O(1)

        # O(n - 1) * O(n) = O(n*n)
        for i in range(len(arr) - 1):# O(n - 1)
            greatest_element_of_right_side = 0
            for j in range(i + 1, len(arr)):# n - 1 + n - 2 + n - 4 = x operations = (n)(n - 1) / 2
                if arr[j] > greatest_element_of_right_side:
                    greatest_element_of_right_side = arr[j]

            arr[i] = greatest_element_of_right_side

        arr[len(arr) - 1] = -1
        return arr

        