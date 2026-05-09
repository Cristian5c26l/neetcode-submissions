class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter = 0
        max_consecutive_1s = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                max_consecutive_1s = max(max_consecutive_1s, counter)
                counter = 0

        max_consecutive_1s = max(max_consecutive_1s, counter)
        return max_consecutive_1s
