class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Time Complexity: O(n)
        # input: [1,2,4]. target = 6. Output: 2. Explanation: The subarray [2, 4] has the minimal length

        # Pattern: Sliding Window Variable size
        curr_sum = 0
        L = 0
        length = float("inf")
        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                length = min(length, R - L + 1)
                curr_sum -= nums[L]
                L += 1
        return 0 if length == float("inf") else length