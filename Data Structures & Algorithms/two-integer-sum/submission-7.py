class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        hash_map = {}# {num: index}. num acts as the difference to future nums participating in the equation target - nums[i]
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map:
                return [hash_map[difference], i]# every input has exactly one pair of indices i and j that satisfy the condition. Returned answer is an array with the smaller index first
            else:
                hash_map[nums[i]] = i

        