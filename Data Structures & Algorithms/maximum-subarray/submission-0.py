class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        max_sum = nums[0]# To track the max_sum over the complete travers of the array nums = [4, -1, 2, -7, 3, 4]
        curr_sum = 0# To track the current sum of each number of the array

        for n in nums:# O(n)
            curr_sum = max(curr_sum, 0)#guarantees avoid negative subarray sum, which allows to re-start the curr_sum to 0 after reach a negative sum which won't be greater that a positive sum
            curr_sum += n# curr_sum = 4 - 1 + 2 - 7 = -2. max_sum = 5. Then curr_sum = 0 + 3 + 4, which is greater than 5, thus the result is 7
            max_sum = max(max_sum, curr_sum)

        return max_sum