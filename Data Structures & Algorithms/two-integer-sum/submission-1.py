class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution
        # Time complexity: O(n*n)
        # Space complexity: O(1)

        res = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break
                j += 1

        return res