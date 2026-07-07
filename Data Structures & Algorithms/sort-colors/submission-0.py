class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Brute Force Solution (by using merge sort + insertion sort)
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n) 
        
        nums.sort()

        
