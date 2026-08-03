class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        L, R = 0, len(nums) - 1

        # Linear Search
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
        