class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      
      # Example of Worst case (Big O Notation): nums = [3,3,3,3,3], 3
      
      # Brute Force Solution
      # Time complexity: O(n*n)
      # Space complexity: O(1)
      nums_length = len(nums)
      i = 0
      while i < nums_length:# i = 0 -> 4 iterations | i = 0 -> 3 iterations ... (n - 1) + (n - 2) + ... + (n - 4) = 4 + 3 + ... + 1 = (n)(n - 1)/2 = 20/2 = 10 iterations of internal for
        #O(n)
        if nums[i] == val:
          for index in range(i + 1, nums_length):# Worst case: O(n)
            nums[index - 1] = nums[index]
          
          nums[nums_length - 1] = -1
          nums_length -= 1
        else:# O(1)
          i += 1

      return nums_length# k