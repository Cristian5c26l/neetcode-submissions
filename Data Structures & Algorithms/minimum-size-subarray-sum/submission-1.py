class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Time Complexity: O(n)
        # input: [1,2,4]. target = 6. Output: 2. Explanation: The subarray [2, 4] has the minimal length

        # Pattern: Sliding Window Variable size
        L, curr_sum = 0, 0
        length = float("inf")

        for R in range(len(nums)):# Expand the window
            curr_sum += nums[R]# Sum the nums while window is expanding (R is increasing, getting away from L)
            while curr_sum >= target:# We have found a valid window (which is a subarray that its sum is greater or equal to the target)
                length = min(R - L + 1, length)
                curr_sum -= nums[L]
                L += 1# Shrink the window
        
        return 0 if length == float("inf") else length