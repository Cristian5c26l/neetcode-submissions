class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Optimal solution
        # Time: O(n)
        # Space: O(1)
        
        max_number_consecutive = 0
        counter = 0
        for num in nums:
            
            if(num == 1):
                counter += 1
                max_number_consecutive = max(max_number_consecutive, counter)
            else:
                counter = 0
            
        return max_number_consecutive
            
