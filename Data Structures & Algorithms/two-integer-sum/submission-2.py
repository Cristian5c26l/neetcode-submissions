class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution
        # Time complexity: O(n*n)
        # Space complexity: O(1)

        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []