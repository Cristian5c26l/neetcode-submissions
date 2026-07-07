class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Optimal Solution (by using bucket sort)
        # Time Complexity: O(n)
        # Space Complexity: O(1) (due to counts array could have space of size constant)
        
        counts = [0] * 3
        for n in nums:# O(n). By the way, n = 0 | 1 | 2
            counts[n] += 1

        # Each index in counts is an element inside the nums array. 
        # Each element in counts is the number of times the counts' index (counts' index = num inside of nums) appears in the nums array

        l = 0# Pointer to overwrite
        for i in range(len(counts)): # O(n). By the way, n = i = 0, 1, 2
            while counts[i]:
                counts[i] -= 1
                nums[l] = i
                l += 1

        
