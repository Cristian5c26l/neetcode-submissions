class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      
      # Example of Worst case (Big O Notation): nums = [3,3,3,3,3], 3
      
      # Optimal Solution with 2 pointers strategy
      # Time complexity: O(n)
      # Space complexity: O(1)
      r = 0# Read
      w = 0# Write
      nums_length = len(nums)
      # O(cn) = O(n)
      while(r < len(nums)):# O(n)
        # O(c)
        if nums[r] == val:
          r += 1
        else:
          nums[w] = nums[r]
          w, r = w + 1, r + 1

      return w