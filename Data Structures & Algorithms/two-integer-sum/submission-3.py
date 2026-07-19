class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal Solution
        # Time complexity: O(n)
        # Space complexity: O(n)

        nums_hash_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums_hash_map:
                return [nums_hash_map[difference], i]
            else:
                nums_hash_map[nums[i]] = i


        return []