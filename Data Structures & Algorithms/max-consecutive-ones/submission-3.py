class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Optimal solution
        # Time: O(n)
        # Space: O(1)
        max_number_consecutive = 0
        counter = 0
        for i in range(len(nums)):
            
            if(nums[i] == 0):
                counter = 0
                continue
            
            counter += 1
            max_number_consecutive = max(max_number_consecutive, counter)


        
        return max_number_consecutive
            
