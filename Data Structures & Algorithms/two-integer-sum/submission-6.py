class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):# j + 1 guarantees i isn't equal to i
                if nums[i] + nums[j] == target:
                    return [i, j]