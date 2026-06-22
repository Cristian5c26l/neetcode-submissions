class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Optimal Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # O(n)
        greatest_element_of_right_side = 0 # Init greatest element on the right side with 0 value due to constraint 1 <= arr[i] <= 100,000 what allows to always the if condition be true
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > greatest_element_of_right_side:
                greatest_element_of_right_side, arr[i] = arr[i], greatest_element_of_right_side 
            else:
                arr[i] = greatest_element_of_right_side

        arr[len(arr) - 1] = -1
        return arr

        