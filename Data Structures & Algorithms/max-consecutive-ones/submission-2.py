class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute force
        # Time: O(n*n), when we for example have nums = [1,1,1,1,1] 
        # Space: O(1)
        max_number_consecutive = 0
        for i in range(len(nums)):
            
            counter = 0
            j = i
            while(j < len(nums) and nums[j] == 1):# Edge cases: j < len(nums)
                j += 1
                counter += 1

            max_number_consecutive = max(max_number_consecutive, counter)
        
        return max_number_consecutive
            
